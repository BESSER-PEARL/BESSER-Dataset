





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Delete extends FileTask {

    private String includes;
    private String quiet;
    private String excludesfile;
    private String failonerror;
    private String dir;
    private String verbose;
    private String file;
    private String includeEmptyDirs;
    private String includesfile;
    private String defaultexcludes;
    private String excludes;



    public MavenMaven_Delete(
        String includes,        String quiet,        String excludesfile,        String failonerror,        String dir,        String verbose,        String file,        String includeEmptyDirs,        String includesfile,        String defaultexcludes,        String excludes    ) {
        super(
        );
        this.includes = includes;
        this.quiet = quiet;
        this.excludesfile = excludesfile;
        this.failonerror = failonerror;
        this.dir = dir;
        this.verbose = verbose;
        this.file = file;
        this.includeEmptyDirs = includeEmptyDirs;
        this.includesfile = includesfile;
        this.defaultexcludes = defaultexcludes;
        this.excludes = excludes;
    }


    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
    }
    public String getQuiet() {
        return quiet;
    }

    public void setQuiet(String quiet) {
        this.quiet = quiet;
    }
    public String getExcludesfile() {
        return excludesfile;
    }

    public void setExcludesfile(String excludesfile) {
        this.excludesfile = excludesfile;
    }
    public String getFailonerror() {
        return failonerror;
    }

    public void setFailonerror(String failonerror) {
        this.failonerror = failonerror;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getVerbose() {
        return verbose;
    }

    public void setVerbose(String verbose) {
        this.verbose = verbose;
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
    public String getIncludesfile() {
        return includesfile;
    }

    public void setIncludesfile(String includesfile) {
        this.includesfile = includesfile;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getExcludes() {
        return excludes;
    }

    public void setExcludes(String excludes) {
        this.excludes = excludes;
    }


}