





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String filtering;
    private String flatten;
    private String todir;
    private String overwrite;
    private String presservelastmodified;
    private String file;
    private String tofile;
    private String includeEmptyDirs;





    private FileSet fileset;


    public Ant_Copy(
        String filtering,        String flatten,        String todir,        String overwrite,        String presservelastmodified,        String file,        String tofile,        String includeEmptyDirs    ) {
        super(
        );
        this.filtering = filtering;
        this.flatten = flatten;
        this.todir = todir;
        this.overwrite = overwrite;
        this.presservelastmodified = presservelastmodified;
        this.file = file;
        this.tofile = tofile;
        this.includeEmptyDirs = includeEmptyDirs;
    }


    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
    }
    public String getFlatten() {
        return flatten;
    }

    public void setFlatten(String flatten) {
        this.flatten = flatten;
    }
    public String getTodir() {
        return todir;
    }

    public void setTodir(String todir) {
        this.todir = todir;
    }
    public String getOverwrite() {
        return overwrite;
    }

    public void setOverwrite(String overwrite) {
        this.overwrite = overwrite;
    }
    public String getPresservelastmodified() {
        return presservelastmodified;
    }

    public void setPresservelastmodified(String presservelastmodified) {
        this.presservelastmodified = presservelastmodified;
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
    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }

    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }

}