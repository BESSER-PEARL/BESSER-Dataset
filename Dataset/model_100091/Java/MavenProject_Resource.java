





import java.util.List;
import java.util.ArrayList;

public class MavenProject_Resource  {

    private String directory;
    private String filtering;
    private String includes;
    private String excludes;
    private String targetPath;



    public MavenProject_Resource(
        String directory,        String filtering,        String includes,        String excludes,        String targetPath    ) {
        this.directory = directory;
        this.filtering = filtering;
        this.includes = includes;
        this.excludes = excludes;
        this.targetPath = targetPath;
    }


    public String getDirectory() {
        return directory;
    }

    public void setDirectory(String directory) {
        this.directory = directory;
    }
    public String getFiltering() {
        return filtering;
    }

    public void setFiltering(String filtering) {
        this.filtering = filtering;
    }
    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
    }
    public String getExcludes() {
        return excludes;
    }

    public void setExcludes(String excludes) {
        this.excludes = excludes;
    }
    public String getTargetpath() {
        return targetPath;
    }

    public void setTargetpath(String targetPath) {
        this.targetPath = targetPath;
    }


}