const path = require("path");

const packagejson = require("./package.json");

const dashLibraryName = packagejson.name.replace(/-/g, "_");

module.exports = function (env, argv) {
  const mode = "development";
  const entry = [path.join(__dirname, "src/demo/index.tsx")];
  const output = {
    filename: "./output.js",
    path: path.resolve(__dirname),
  };

  const externals = undefined;

  return {
    output,
    mode,
    entry,
    target: "web",
    externals,
    devtool: "inline-source-map",
    devServer: {
      static: {
        directory: path.join(__dirname, "/"),
      },
    },
    resolve: {
      extensions: [".ts", ".tsx", ".js", ".jsx", ".json"],
    },
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          use: "ts-loader",
          exclude: /node_modules/,
        },
        {
          test: /\.css$/,
          use: [
            {
              loader: "style-loader",
              options: {
                insert: function insertAtTop(element) {
                  var parent = document.querySelector("head");
                  var lastInsertedElement =
                    window._lastElementInsertedByStyleLoader;

                  if (!lastInsertedElement) {
                    parent.insertBefore(element, parent.firstChild);
                  } else if (lastInsertedElement.nextSibling) {
                    parent.insertBefore(
                      element,
                      lastInsertedElement.nextSibling
                    );
                  } else {
                    parent.appendChild(element);
                  }

                  window._lastElementInsertedByStyleLoader = element;
                },
              },
            },
            {
              loader: "css-loader",
            },
          ],
        },
        {
          test: /\.tsv$/,
          use: [{ loader: "file-loader" }],
        },
      ],
    },
  };
};
