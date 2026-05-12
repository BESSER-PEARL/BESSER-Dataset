





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Delete extends FileTask {

    private String quiet;
    private String excludes;
    private String failonerror;
    private String includeEmptyDirs;
    private String dir;
    private String includes;
    private String file;
    private String verbose;
    private String excludesfile;
    private String includesfile;
    private String defaultexcludes;



    public MavenMaven_Delete(
        String quiet,        String excludes,        String failonerror,        String includeEmptyDirs,        String dir,        String includes,        String file,        String verbose,        String excludesfile,        String includesfile,        String defaultexcludes    ) {
        super(
        );
        this.quiet = quiet;
        this.excludes = excludes;
        this.failonerror = failonerror;
        this.includeEmptyDirs = includeEmptyDirs;
        this.dir = dir;
        this.includes = includes;
        this.file = file;
        this.verbose = verbose;
        this.excludesfile = excludesfile;
        this.includesfile = includesfile;
        this.defaultexcludes = defaultexcludes;
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
    public String getFailonerror() {
        return failonerror;
    }

    public void setFailonerror(String failonerror) {
        this.failonerror = failonerror;
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
    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getVerbose() {
        return verbose;
    }

    public void setVerbose(String verbose) {
        this.verbose = verbose;
    }
    public String getExcludesfile() {
        return excludesfile;
    }

    public void setExcludesfile(String excludesfile) {
        this.excludesfile = excludesfile;
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


}