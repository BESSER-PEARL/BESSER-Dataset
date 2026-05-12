





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String overwrite;
    private String filtering;
    private String todir;
    private String presservelastmodified;
    private String file;
    private String includeEmptyDirs;
    private String flatten;
    private String tofile;



    public Ant_Copy(
        String overwrite,        String filtering,        String todir,        String presservelastmodified,        String file,        String includeEmptyDirs,        String flatten,        String tofile    ) {
        super(
        );
        this.overwrite = overwrite;
        this.filtering = filtering;
        this.todir = todir;
        this.presservelastmodified = presservelastmodified;
        this.file = file;
        this.includeEmptyDirs = includeEmptyDirs;
        this.flatten = flatten;
        this.tofile = tofile;
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


}