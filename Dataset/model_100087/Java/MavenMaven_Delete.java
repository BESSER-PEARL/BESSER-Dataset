





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Delete extends FileTask {

    private String includeEmptyDirs;
    private String excludes;
    private String verbose;
    private String excludesfile;
    private String file;
    private String failonerror;
    private String includesfile;
    private String dir;
    private String defaultexcludes;
    private String quiet;
    private String includes;



    public MavenMaven_Delete(
        String includeEmptyDirs,        String excludes,        String verbose,        String excludesfile,        String file,        String failonerror,        String includesfile,        String dir,        String defaultexcludes,        String quiet,        String includes    ) {
        super(
        );
        this.includeEmptyDirs = includeEmptyDirs;
        this.excludes = excludes;
        this.verbose = verbose;
        this.excludesfile = excludesfile;
        this.file = file;
        this.failonerror = failonerror;
        this.includesfile = includesfile;
        this.dir = dir;
        this.defaultexcludes = defaultexcludes;
        this.quiet = quiet;
        this.includes = includes;
    }


    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
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
    public String getExcludesfile() {
        return excludesfile;
    }

    public void setExcludesfile(String excludesfile) {
        this.excludesfile = excludesfile;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
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
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getQuiet() {
        return quiet;
    }

    public void setQuiet(String quiet) {
        this.quiet = quiet;
    }
    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
    }


}