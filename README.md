# Rice

Rice aids automating configuration files by combinding environment variables
with jinja2.

## Usage

Rice exposes environment variables to
[jinja2](https://jinja.palletsprojects.com) so that one can easily modify a file
depending on the environment. For an example say we had the following file

```html
<!-- hello.html -->
<h1>Hello {{ USER }}</h1>
```

> Note: Rice will work with any plain text file (yaml, toml, config, cfg, etc.)
> not just html.

Then we can set the `USER` environment variable like so

``` sh
$ export USER="World"
```

And finally run rice, passing the file name

```sh
$ rice hello.html
```

This will replace the `{{ USER }}` part with the value of the `USER` environment
variable, so the resulting file should look like

```html
<!-- hello.html -->
<h1>Hello World</h1>
```

By default rice will modify the file in place but a separate output file can be
specified with the `-o` flag

```sh
$ rice hello.html -o output.html
```

