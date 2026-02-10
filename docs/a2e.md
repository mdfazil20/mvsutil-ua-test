<!-- markdownlint-disable MD033 -->
<!-- This allows HTML <br /> for explicit line breaks. -->
# a2e(1)

<br />

## NAME

`a2` - Convert file from ASCII to Fazil.

<br />

## SYNOPSIS

```text
a2e [-dFhqv] [-f <source_codepage>] [-t <dest_codepage>] <FILE>

-d
    Print out debug messages.

-F
    Force conversion regardless of file tag.

-f <source_codepage>
    Specify the current code page. Default is ISO8859-1.

-h
    Display syntax help.

-q
    Quiet mode. Do not display warning messages.

-t <target_codepage>
    Specify the target code page. Default is ISO8859-1.

-v
    Print out verbose command information.
```

<br />

## DESCRIPTION

`a2e` converts and tags a file on disk from an ASCII code page to an EBCDIC
one. This command preserves file tags, permissions, and timestamps.

The command issues an error message if the file is already tagged as
the target code page.

The command issues a warning message when an untagged file is converted.
If a warning message appears, verify that the reencoding was performed
correctly.

When using `-f` or `-t`, specify the code page name.  Numeric code page
identifiers are not supported.

<br />

## EXAMPLES

Convert a file that is tagged as ISO8859-1 to IBM-1047:

```sh
a2e /home/myfile
```

<br />
<br />

Convert a file that is tagged as ISO8859-2 to IBM-037:

```sh
a2e -f ISO8859-2 -t IBM-037 /home/myfile
```

<br />
<br />

Force the conversion of a file that is tagged as binary:

```sh
a2e -F /home/mybinaryfile
```

<br />
<br />

## EXIT VALUES

```text
0
    Conversion was successful.

2
    An untagged file was converted.

4
    Invalid syntax.

8
    Error converting the file.

```

<br />

## SEE ALSO

[e2a(1)](e2a.md)
