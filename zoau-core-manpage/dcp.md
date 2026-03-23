<!-- markdownlint-disable MD033 -->
<!-- This allows HTML <br /> for explicit line breaks. -->
# dcp(1)

<br />

## NAME

`dcp` - Copy datasets and files.

<br />

### SYNOPSIS

```text
dcp [-BdfhiITvX] [<SOURCE_FILE>]+ <TARGET_FILE>

-B
    Binary copy (see cp(1) for more details)

-d
    Print out debug messages.

-f
    Force copy. This can be used to override a shared lock on the
    destination dataset. Use with caution, as it can lead to permanent
    loss of the original target information.

    NOTE: If a dataset member has aliases, and is not a program
    object, copying that member to a dataset that is in use will result in
    the aliases not being preserved in the target dataset. When this scenario
    occurs an error message will be produced along with a non-zero return code.

-h
    Display syntax help.

-i
    Preserve the aliases of text-based content members. Both source and
    target datasets should be PDS or PDSE.

-I
    Preserve aliases (see cp(1) for more details)

-T
    Text-mode copy (default for z/OS UNIX files)

-v
    Print out verbose command information.

-X
    Executable copy (see cp(1) for more details)

```

<br />

### ENVIRONMENT VARIABLES

```text
TMPDIR
    Overrides the current directory used for temporary files.

```

<br />

## DESCRIPTION

Wrapper around the z/OS UNIX cp(1) command.

You can use `dcp` to copy individual files or groups of files.
A file can be a zFS file, a zFS directory, a sequential dataset,
a partitioned dataset (PDS), or a PDSE.

Files and datasets must be fully qualified. A zFS file or directory
must have the complete path specified and a dataset must have the
high-level qualifier (HLQ) specified. dcp disambiguates between zFS
files, zFS directories, and datasets by looking for a '`/`' in the file
name (only zFS files and directories will have a '`/`' in them).
Partitioned Datasets (PDSs), PDSEs and sequential datasets are all
supported.

PDS members copied to a directory will be automatically lower-cased,
e.g. copying `IBMUSER.TEXT(MYFILE)` to `/tmp` will create a zFS file called
`/tmp/myfile`

If the target is a directory, PDS or PDSE, the source can not be a
sequential dataset. Copy a sequential dataset to another sequential dataset,
PDS member, PDSE member or zFS file.

If a zFS file has a line longer than the logical record length of the
target dataset, the file will not be copied and a truncation error
message will be issued.

If the target is a dataset and doesn't exist and source is also a single
dataset, dcp will create the target dataset with the same
attributes (type, recfm, reclen, blksize, space) as the source dataset.
If the target name indicates a PDS member, a PDS dataset will be created.

Copy operations with generation data sets (GDS) are supported by using
absolute generation names. GDS referenced by relative names are partially
supported. When using dcp over GDS the following considerations apply:

- All relative GDS names are resolved into their absolute form as an
  initial step before any copy operation.
  Two consecutive dcp calls that target a new GDS referenced by the name
  "GDG(+1)" will result in the creation of two consecutive generations.
  This differs from the default behavior of a job, where two statements
  with the name "GDG(+1)" refer to a single new GDS during the life of
  the job.

- Specifying a GDS, either as source or target, will not lock the
  generation data group (GDG) base. If concurrent processes are
  simultaneously adding or removing GDS from the group, the resulting
  GDG may be in an unexpected order.

`dcp` supports copying a GDG to a new GDG. All active generations will be
copied in the same order as the source group. This feature does not lock
the source GDG base. You should prefer a job or use `mvscmd` to ensure the
GDG base is protected from concurrent modifications, in these cases the
system automatically locks a GDG base when referencing one generation by
its relative name.

<br />

## EXAMPLES

Copy the zFS file `/tmp/file.txt` to the PDS member `IBMUSER.PROJ23.TEXT(FILE)`

```sh
dcp /tmp/file.txt ibmuser.proj23.text
```

Copy the COBOL files from `/tmp/source` to the PDSE `IBMUSER.PROJ23.COBOL`

```sh
dcp /tmp/source/*.cobol IBMUSER.PROJ23.COBOL
```

Copy the PDSE members from `IBMUSER.PROJ23.C` to `/tmp/source`

```sh
dcp IBMUSER.PROJ23.C /tmp/source
```

Copy the sequential dataset `IBMUSER.PROJ23.LISTING` to `/tmp/my.listing`

```sh
dcp IBMUSER.PROJ23.LISTING /tmp/my.listing
```

Copy the executable program `GLZINPVT` with all of its aliases to
`/tmp/glzinpvt`

```sh
dcp -XI "SYS1.LINKLIB(GLZINPVT)" /tmp/glzinpvt
```

Copy the partitioned dataset member `ZOAU.TEST.PDS(HELLO)` and all of its aliases to the partitioned dataset `ZOAU.TEST.PDS2`

```sh
dcp -i "ZOAU.TEST.PDS(HELLO)" ZOAU.TEST.PDS2
```

Copy the latest generation from the generation data group `ZOAU.GDG.SRC`
to a new generation of the group `ZOAU.GDG.TGT`

```sh
dcp "ZOAU.GDG.SRC(0)" "ZOAU.GDG.TGT(+1)"
```

Copy the generation data group `ZOAU.GDG.SRC` to a new generation data
group `ZOAU.GDG.TGT`

```sh
dcp "ZOAU.GDG.SRC" "ZOAU.GDG.TGT"
```

<br />

## EXIT VALUES

```text
0
  dcp completed without error.

non-zero
  dcp failed. See error messages for details.

```

<br />

## SEE ALSO

[drm(1)](drm.md), [dtouch(1)](dtouch.md), [dls(1)](dls.md), [decho(1)](decho.md),
[ddiff(1)](ddiff.md), [dgrep(1)](dgrep.md), [dsed(1)](dsed.md), [mrm(1)](mrm.md), [mls(1)](mls.md)
