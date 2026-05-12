





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String file;
    private String includeEmptyDirs;
    private String tofile;
    private String overwrite;
    private String flatten;
    private String todir;
    private String presservelastmodified;
    private String filtering;



    public Ant_Copy(
        String file,        String includeEmptyDirs,        String tofile,        String overwrite,        String flatten,        String todir,        String presservelastmodified,        String filtering    ) {
        super(
        );
        this.file = file;
        this.includeEmptyDirs = includeEmptyDirs;
        this.tofile = tofile;
        this.overwrite = overwrite;
        this.flatten = flatten;
        this.todir = todir;
        this.presservelastmodified = presservelastmodified;
        this.filtering = filtering;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }
    public String getTofile() {
        return tofile;
    }

    public void setTofile(String tofile) {
        this.tofile = tofile;
    }
    public String getOverwrite() {
        return overwrite;
    }

    public void setOverwrite(String overwrite) {
        this.overwrite = overwrite;
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
    public String getPresservelastmodified() {
        return presservelastmodified;
    }

    public void setPresservelastmodified(String presservelastmodified) {
        this.presservelastmodified = presservelastmodified;
    }
    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
    }


}