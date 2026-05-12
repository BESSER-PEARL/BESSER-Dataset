





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Copy extends FileTask {

    private String tofile;
    private String flatten;
    private String filtering;
    private String file;
    private String includeEmptyDirs;
    private String presservelastmodified;
    private String todir;
    private String overwrite;





    private MavenMaven_FileSet mavenmaven_fileset;




    private MavenMaven_Mapper mavenmaven_mapper;




    private MavenMaven_FilterSet mavenmaven_filterset;


    public MavenMaven_Copy(
        String tofile,        String flatten,        String filtering,        String file,        String includeEmptyDirs,        String presservelastmodified,        String todir,        String overwrite    ) {
        super(
        );
        this.tofile = tofile;
        this.flatten = flatten;
        this.filtering = filtering;
        this.file = file;
        this.includeEmptyDirs = includeEmptyDirs;
        this.presservelastmodified = presservelastmodified;
        this.todir = todir;
        this.overwrite = overwrite;
    }


    public String getTofile() {
        return tofile;
    }

    public void setTofile(String tofile) {
        this.tofile = tofile;
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

    public MavenMaven_FileSet getMavenmaven_fileset() {
        return mavenmaven_fileset;
    }

    public void setMavenmaven_fileset(MavenMaven_FileSet mavenmaven_fileset) {
        this.mavenmaven_fileset = mavenmaven_fileset;
    }
    public MavenMaven_Mapper getMavenmaven_mapper() {
        return mavenmaven_mapper;
    }

    public void setMavenmaven_mapper(MavenMaven_Mapper mavenmaven_mapper) {
        this.mavenmaven_mapper = mavenmaven_mapper;
    }
    public MavenMaven_FilterSet getMavenmaven_filterset() {
        return mavenmaven_filterset;
    }

    public void setMavenmaven_filterset(MavenMaven_FilterSet mavenmaven_filterset) {
        this.mavenmaven_filterset = mavenmaven_filterset;
    }

}