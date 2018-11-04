# JsModules

> [JsModules] is a Sublime Text Plug-in to convert CJS modules to ES modules.

## Installation

[JsModules] is compatible with both Sublime Text 2 and 3, and all supported
Operating Systems.

### Requirements

- [Sublime Text] - Text editor for code
- [node.js] - JavaScript runtime
- [yarn] or [npm] - Package manager for JavaScript
- [cjs-to-es6] - CLI to convert JavaScript files from CommonJS to ES6 modules

### Install cjs-to-es6

If you installed [cjs-to-es6] globally (using the [yarn] or [npm] command below), there's nothing else you need to do.

```bash
# using yarn:
yarn global add cjs-to-es6

# using npm:
npm install -g cjs-to-es6
```

### Install JsModules via Package Control

The easiest and recommended way to install Js​Modules is using [Package Control].

From the **main application menu**, navigate to:

- `Tools` -> `Command Palette...` -> `Package Control: Install Package`, type
  the word **JsModules**, then select it to complete the installation.

### Install JsModules Manually

1. Download and extract Js​Modules [zip file] to your [Sublime Text Packages directory].
2. Rename the extracted directory from `SublimeJsModules-master` to `JsModules`.

**Default Sublime Text Packages Paths:**
<a name="default-st-paths"></a>

- **OS X:** `~/Library/Application Support/Sublime Text [2|3]/Packages`
- **Linux:** `~/.Sublime Text [2|3]/Packages`
- **Windows:** `%APPDATA%/Sublime Text [2|3]/Packages`

> **NOTE** Replace the `[2|3]` part with the appropriate Sublime Text
> version for your installation.

## Usage

To run the `JsModules` command... open the Sublime Text **Command Palette**
(<kbd>super + shift + p</kbd>) and type ***JsModules: Convert file to ES module***.
