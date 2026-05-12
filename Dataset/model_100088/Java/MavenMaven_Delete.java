





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Delete extends FileTask {

    private String includesfile;
    private String includes;
    private String includeEmptyDirs;
    private String quiet;
    private String defaultexcludes;
    private String failonerror;
    private String excludes;
    private String dir;
    private String file;
    private String excludesfile;
    private String verbose;



    public MavenMaven_Delete(
        String includesfile,        String includes,        String includeEmptyDirs,        String quiet,        String defaultexcludes,        String failonerror,        String excludes,        String dir,        String file,        String excludesfile,        String verbose    ) {
        super(
        );
        this.includesfile = includesfile;
        this.includes = includes;
        this.includeEmptyDirs = includeEmptyDirs;
        this.quiet = quiet;
        this.defaultexcludes = defaultexcludes;
        this.failonerror = failonerror;
        this.excludes = excludes;
        this.dir = dir;
        this.file = file;
        this.excludesfile = excludesfile;
        this.verbose = verbose;
    }


    public String getIncludesfile() {
        return includesfile;
    }

    public void setIncludesfile(String includesfile) {
        this.includesfile = includesfile;
    }
    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
    }
    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }
    public String getQuiet() {
        return quiet;
    }

    public void setQuiet(String quiet) {
        this.quiet = quiet;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getFailonerror() {
        return failonerror;
    }

    public void setFailonerror(String failonerror) {
        this.failonerror = failonerror;
    }
    public String getExcludes() {
        return excludes;
    }

    public void setExcludes(String excludes) {
        this.excludes = excludes;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getExcludesfile() {
        return excludesfile;
    }

    public void setExcludesfile(String excludesfile) {
        this.excludesfile = excludesfile;
    }
    public String getVerbose() {
        return verbose;
    }

    public void setVerbose(String verbose) {
        this.verbose = verbose;
    }


}