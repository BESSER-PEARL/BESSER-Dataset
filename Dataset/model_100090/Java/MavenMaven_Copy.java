





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Copy extends FileTask {

    private String includeEmptyDirs;
    private String overwrite;
    private String file;
    private String flatten;
    private String tofile;
    private String filtering;
    private String todir;
    private String presservelastmodified;





    private FileSet fileset;


    public MavenMaven_Copy(
        String includeEmptyDirs,        String overwrite,        String file,        String flatten,        String tofile,        String filtering,        String todir,        String presservelastmodified    ) {
        super(
        );
        this.includeEmptyDirs = includeEmptyDirs;
        this.overwrite = overwrite;
        this.file = file;
        this.flatten = flatten;
        this.tofile = tofile;
        this.filtering = filtering;
        this.todir = todir;
        this.presservelastmodified = presservelastmodified;
    }


    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
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

    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }

}