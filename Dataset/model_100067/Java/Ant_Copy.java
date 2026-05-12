





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String overwrite;
    private String todir;
    private String filtering;
    private String includeEmptyDirs;
    private String file;
    private String flatten;
    private String tofile;
    private String presservelastmodified;





    private FileSet fileset;


    public Ant_Copy(
        String overwrite,        String todir,        String filtering,        String includeEmptyDirs,        String file,        String flatten,        String tofile,        String presservelastmodified    ) {
        super(
        );
        this.overwrite = overwrite;
        this.todir = todir;
        this.filtering = filtering;
        this.includeEmptyDirs = includeEmptyDirs;
        this.file = file;
        this.flatten = flatten;
        this.tofile = tofile;
        this.presservelastmodified = presservelastmodified;
    }


    public String getOverwrite() {
        return overwrite;
    }

    public void setOverwrite(String overwrite) {
        this.overwrite = overwrite;
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
    public String getFlatten() {
        return flatten;
    }

    public void setFlatten(String flatten) {
        this.flatten = flatten;
    }
    public String getTofile() {
        return tofile;
    }

    public void setTofile(String tofile) {
        this.tofile = tofile;
    }
    public String getPresservelastmodified() {
        return presservelastmodified;
    }

    public void setPresservelastmodified(String presservelastmodified) {
        this.presservelastmodified = presservelastmodified;
    }

    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }

}