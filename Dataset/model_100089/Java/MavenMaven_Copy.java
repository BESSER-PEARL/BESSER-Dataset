





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Copy extends FileTask {

    private String file;
    private String todir;
    private String includeEmptyDirs;
    private String flatten;
    private String presservelastmodified;
    private String filtering;
    private String overwrite;
    private String tofile;





    private FilterSet filterset;




    private Mapper mapper;




    private FileSet fileset;


    public MavenMaven_Copy(
        String file,        String todir,        String includeEmptyDirs,        String flatten,        String presservelastmodified,        String filtering,        String overwrite,        String tofile    ) {
        super(
        );
        this.file = file;
        this.todir = todir;
        this.includeEmptyDirs = includeEmptyDirs;
        this.flatten = flatten;
        this.presservelastmodified = presservelastmodified;
        this.filtering = filtering;
        this.overwrite = overwrite;
        this.tofile = tofile;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
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
    public String getFlatten() {
        return flatten;
    }

    public void setFlatten(String flatten) {
        this.flatten = flatten;
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
    public String getTofile() {
        return tofile;
    }

    public void setTofile(String tofile) {
        this.tofile = tofile;
    }

    public FilterSet getFilterset() {
        return filterset;
    }

    public void setFilterset(FilterSet filterset) {
        this.filterset = filterset;
    }
    public Mapper getMapper() {
        return mapper;
    }

    public void setMapper(Mapper mapper) {
        this.mapper = mapper;
    }
    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }

}