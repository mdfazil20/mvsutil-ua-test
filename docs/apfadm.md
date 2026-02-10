<!-- markdownlint-disable MD033 -->
<!-- This allows HTML <br /> for explicit line breaks. -->
# apfadm(1)

<br />

## NAME

`apfadm` - Authorized Program Facility (APF) administration.

<br />

## SYNOPSIS

```text
apfadm [-dfhijJlv] [-[AD] <ds,vol> | <ds,sms> | <ds>]* [-M <marker>]
       [-[PR] <dataset> ] [-F [DYNAMIC|STATIC]]

-A/-D <ds,vol | ds,SMS | ds>
  Add or remove a dataset to or from the APF list. This argument can be in
  three formats:
    <ds,vol | ds,SMS | ds>

  If a volume serial or SMS was not specified, the program will try to
  find out the volume serial or SMS.

-d
  Enable debug output.

-f
  Force set the list format to DYNAMIC before add or remove operation.
  Only effective when -A or -D is used.

-F [DYNAMIC|STATIC]
  Set APF list format to DYNAMIC or STATIC. Print current format if
  bvalue is omitted.

-h
  Print this syntax message.

-i
  Ignore errors if dataset is already present during add operation or
  missing during delete operation.

-j
  Print APF list in JSON format (should be used with -l)
  Example:
    { "data": { "format": "DYNAMIC", "header": ['<1st line>', ... ],
      datasets: [ { "vol":"G2201D", "ds": "SYS1.LINKLIB" }, ... ] } }

-J
  Print JSON output in a readable format. This option enables -j if it
  was not specified.

-l
  Print APF list.

-M <marker>
  Custom marker in "\/\*.*{mark}.*\*\/" format,
  default: "/* {mark} MANAGED BLOCK <timestamp> */"
  <timestamp> will be replaced with current time, format: "+%Y%m%d-%H%M%S"

-P <dataset>
  The dataset used to persist the APF entry.

-R <dataset>
  The dataset used to remove the APF entry.
```

<br />

## DESCRIPTION

Authorized Program Facility Admin (`apfadm`) is a tool for:

1. Adding or removing libraries to or from the authorized list.
2. Making the entry persistent or removing an entry from a persistent dataset.
3. Making the list format DYNAMIC or STATIC.
4. Printing the current authorized list.

<br />

## EXAMPLES

Add the dataset IBMUSER.LINKLIB to the list:

```sh
apfadm -A IBMUSER.LINKLIB
```

<br />
<br />

Remove the dataset IBMUSER.LINKLIB from the list:

```sh
  apfadm -D IBMUSER.LINKLIB
```

<br />
<br />

Print current list in JSON format:

```sh
apfadm -lj
```

<br />
<br />

Add and remove libraries to the list and persistent dataset:

```sh
apfadm -A lib1,vol1 -D lib3,vol3 -A lib2,sms -A lib5 -D lib4,vol4 -P "IBMUSER.PDS(MEM)" -R "IBMUSER.PDS2(MEM)"
```

<br />
<br />

Add libraries to the list and persistent dataset with custom marker:

```sh
apfadm -A lib1,vol1 -A lib2,vol2 -M "/* {mark} USR001 PGM001 */" -P "IBMUSER.PDS(MEM)"
```

<br />
<br />

Set the list format to DYNAMIC:

```sh
apfadm -F DYNAMIC
```

<br />
<br />

## EXIT VALUES

```text
0
  apfadm successfully applied the command to the dataset.

2
  Syntax error.

4
  Unknown option or bad argument specified.

other
  Error occurred. See error messages for details.
```

<br />

## SEE ALSO

[opercmd(1)](opercmd.md), [dls(1)](dls.md)
