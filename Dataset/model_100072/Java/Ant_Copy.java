





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String tofile;
    private String todir;
    private String file;
    private String includeEmptyDirs;
    private String presservelastmodified;
    private String filtering;
    private String overwrite;
    private String flatten;





    private FileSet fileset;


    public Ant_Copy(
        String tofile,        String todir,        String file,        String includeEmptyDirs,        String presservelastmodified,        String filtering,        String overwrite,        String flatten    ) {
        super(
        );
        this.tofile = tofile;
        this.todir = todir;
        this.file = file;
        this.includeEmptyDirs = includeEmptyDirs;
        this.presservelastmodified = presservelastmodified;
        this.filtering = filtering;
        this.overwrite = overwrite;
        this.flatten = flatten;
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

    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }

}