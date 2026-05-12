





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Delete extends FileTask {

    private String includes;
    private String excludesfile;
    private String failonerror;
    private String includesfile;
    private String quiet;
    private String excludes;
    private String verbose;
    private String file;
    private String defaultexcludes;
    private String includeEmptyDirs;
    private String dir;



    public MavenMaven_Delete(
        String includes,        String excludesfile,        String failonerror,        String includesfile,        String quiet,        String excludes,        String verbose,        String file,        String defaultexcludes,        String includeEmptyDirs,        String dir    ) {
        super(
        );
        this.includes = includes;
        this.excludesfile = excludesfile;
        this.failonerror = failonerror;
        this.includesfile = includesfile;
        this.quiet = quiet;
        this.excludes = excludes;
        this.verbose = verbose;
        this.file = file;
        this.defaultexcludes = defaultexcludes;
        this.includeEmptyDirs = includeEmptyDirs;
        this.dir = dir;
    }


    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
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
    public String getIncludesfile() {
        return includesfile;
    }

    public void setIncludesfile(String includesfile) {
        this.includesfile = includesfile;
    }
    public String getQuiet() {
        return quiet;
    }

    public void setQuiet(String quiet) {
        this.quiet = quiet;
    }
    public String getExcludes() {
        return excludes;
    }

    public void setExcludes(String excludes) {
        this.excludes = excludes;
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
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }


}