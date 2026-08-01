# Force UTF-8 as the default IO encoding.
#
# When the shell has no LANG/LC_ALL set, Ruby falls back to US-ASCII and
# jekyll-jupyter-notebook crashes reading nbconvert's UTF-8 output with
# "invalid byte sequence in US-ASCII".
Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8
