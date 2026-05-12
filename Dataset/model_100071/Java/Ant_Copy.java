





import java.util.List;
import java.util.ArrayList;

public class Ant_Copy extends FileTask {

    private String presservelastmodified;
    private String file;
    private String includeEmptyDirs;
    private String filtering;
    private String overwrite;
    private String flatten;
    private String tofile;
    private String todir;





    private Ant_Mapper ant_mapper;




    private Ant_FileSet ant_fileset;




    private Ant_FilterSet ant_filterset;


    public Ant_Copy(
        String presservelastmodified,        String file,        String includeEmptyDirs,        String filtering,        String overwrite,        String flatten,        String tofile,        String todir    ) {
        super(
        );
        this.presservelastmodified = presservelastmodified;
        this.file = file;
        this.includeEmptyDirs = includeEmptyDirs;
        this.filtering = filtering;
        this.overwrite = overwrite;
        this.flatten = flatten;
        this.tofile = tofile;
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

    public Ant_Mapper getAnt_mapper() {
        return ant_mapper;
    }

    public void setAnt_mapper(Ant_Mapper ant_mapper) {
        this.ant_mapper = ant_mapper;
    }
    public Ant_FileSet getAnt_fileset() {
        return ant_fileset;
    }

    public void setAnt_fileset(Ant_FileSet ant_fileset) {
        this.ant_fileset = ant_fileset;
    }
    public Ant_FilterSet getAnt_filterset() {
        return ant_filterset;
    }

    public void setAnt_filterset(Ant_FilterSet ant_filterset) {
        this.ant_filterset = ant_filterset;
    }

}