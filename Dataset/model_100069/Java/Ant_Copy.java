





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String presservelastmodified;
    private String todir;
    private String flatten;
    private String overwrite;
    private String filtering;
    private String tofile;
    private String includeEmptyDirs;
    private String file;





    private FileSet fileset;


    public Ant_Copy(
        String presservelastmodified,        String todir,        String flatten,        String overwrite,        String filtering,        String tofile,        String includeEmptyDirs,        String file    ) {
        super(
        );
        this.presservelastmodified = presservelastmodified;
        this.todir = todir;
        this.flatten = flatten;
        this.overwrite = overwrite;
        this.filtering = filtering;
        this.tofile = tofile;
        this.includeEmptyDirs = includeEmptyDirs;
        this.file = file;
    }


    public String getPresservelastmodified() {
        return presservelastmodified;
    }

    public void setPresservelastmodified(String presservelastmodified) {
        this.presservelastmodified = presservelastmodified;
    }
    public String getTodir() {
        return todir;
    }

    public void setTodir(String todir) {
        this.todir = todir;
    }
    public String getFlatten() {
        return flatten;
    }

    public void setFlatten(String flatten) {
        this.flatten = flatten;
    }
    public String getOverwrite() {
        return overwrite;
    }

    public void setOverwrite(String overwrite) {
        this.overwrite = overwrite;
    }
    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
    }
    public String getTofile() {
        return tofile;
    }

    public void setTofile(String tofile) {
        this.tofile = tofile;
    }
    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }

    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }

}