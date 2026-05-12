





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Copy extends FileTask {

    private String filtering;
    private String presservelastmodified;
    private String flatten;
    private String file;
    private String overwrite;
    private String tofile;
    private String todir;
    private String includeEmptyDirs;





    private FileSet fileset;


    public MavenMaven_Copy(
        String filtering,        String presservelastmodified,        String flatten,        String file,        String overwrite,        String tofile,        String todir,        String includeEmptyDirs    ) {
        super(
        );
        this.filtering = filtering;
        this.presservelastmodified = presservelastmodified;
        this.flatten = flatten;
        this.file = file;
        this.overwrite = overwrite;
        this.tofile = tofile;
        this.todir = todir;
        this.includeEmptyDirs = includeEmptyDirs;
    }


    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
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
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getOverwrite() {
        return overwrite;
    }

    public void setOverwrite(String overwrite) {
        this.overwrite = overwrite;
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