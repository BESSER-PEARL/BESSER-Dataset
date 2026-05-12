





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Copy extends FileTask {

    private String tofile;
    private String file;
    private String todir;
    private String presservelastmodified;
    private String overwrite;
    private String flatten;
    private String filtering;
    private String includeEmptyDirs;





    private FilterSet filterset;




    private FileSet fileset;




    private Mapper mapper;


    public MavenMaven_Copy(
        String tofile,        String file,        String todir,        String presservelastmodified,        String overwrite,        String flatten,        String filtering,        String includeEmptyDirs    ) {
        super(
        );
        this.tofile = tofile;
        this.file = file;
        this.todir = todir;
        this.presservelastmodified = presservelastmodified;
        this.overwrite = overwrite;
        this.flatten = flatten;
        this.filtering = filtering;
        this.includeEmptyDirs = includeEmptyDirs;
    }


    public String getTofile() {
        return tofile;
    }

    public void setTofile(String tofile) {
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
    public String getPresservelastmodified() {
        return presservelastmodified;
    }

    public void setPresservelastmodified(String presservelastmodified) {
        this.presservelastmodified = presservelastmodified;
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

    public FilterSet getFilterset() {
        return filterset;
    }

    public void setFilterset(FilterSet filterset) {
        this.filterset = filterset;
    }
    public FileSet getFileset() {
        return fileset;
    }

    public void setFileset(FileSet fileset) {
        this.fileset = fileset;
    }
    public Mapper getMapper() {
        return mapper;
    }

    public void setMapper(Mapper mapper) {
        this.mapper = mapper;
    }

}