





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String includeEmptyDirs;
    private String presservelastmodified;
    private String flatten;
    private String overwrite;
    private String file;
    private String tofile;
    private String todir;
    private String filtering;





    private FileSet fileset;


    public Ant_Copy(
        String includeEmptyDirs,        String presservelastmodified,        String flatten,        String overwrite,        String file,        String tofile,        String todir,        String filtering    ) {
        super(
        );
        this.includeEmptyDirs = includeEmptyDirs;
        this.presservelastmodified = presservelastmodified;
        this.flatten = flatten;
        this.overwrite = overwrite;
        this.file = file;
        this.tofile = tofile;
        this.todir = todir;
        this.filtering = filtering;
    }


    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }
    public String getPresservelastmodified() {
        return presservelastmodified;
    }

    public void setPresservelastmodified(String presservelastmodified) {
        this.presservelastmodified = presservelastmodified;
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
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getTofile() {
        return tofile;
    }

    public void setTofile(String tofile) {
        this.tofile = tofile;
    }
    public String getTodir() {
        return todir;
    }

    public void setTodir(String todir) {
        this.todir = todir;
    }
    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
    }

    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }

}