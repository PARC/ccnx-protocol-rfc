
# Community ICN specifications

These are the protocol specifications related to the [Community ICN](https://wiki.fd.io/view/Cicn) project.

The draft sources are in the `src/` directory and the built draft output is in the `build/` directory.  The
drafts are also available on the gh-pages site.

# Editing

Inside each draft, you should use the suffix '-latest' in the draft name, for example:
```
<rfc category="exp" docName="draft-irtf-icnrg-ccnxmessages-latest" ipr="trust200902">
```

To build the documents, cd in to the `src/` directory and run make.  This will download a subproject
to build the system.  It will replace the `build/` directory.

