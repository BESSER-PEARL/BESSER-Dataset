





import java.util.List;
import java.util.ArrayList;

public class Ant_Delete extends FileTask {

    private String failonerror;
    private String excludes;
    private String quiet;
    private String includeEmptyDirs;
    private String defaultexcludes;
    private String dir;
    private String excludesfile;
    private String file;
    private String includes;
    private String verbose;
    private String includesfile;



    public Ant_Delete(
        String failonerror,        String excludes,        String quiet,        String includeEmptyDirs,        String defaultexcludes,        String dir,        String excludesfile,        String file,        String includes,        String verbose,        String includesfile    ) {
        super(
        );
        this.failonerror = failonerror;
        this.excludes = excludes;
        this.quiet = quiet;
        this.includeEmptyDirs = includeEmptyDirs;
        this.defaultexcludes = defaultexcludes;
        this.dir = dir;
        this.excludesfile = excludesfile;
        this.file = file;
        this.includes = includes;
        this.verbose = verbose;
        this.includesfile = includesfile;
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
    public String getQuiet() {
        return quiet;
    }

    public void setQuiet(String quiet) {
        this.quiet = quiet;
    }
    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
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
    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
    }
    public String getVerbose() {
        return verbose;
    }

    public void setVerbose(String verbose) {
        this.verbose = verbose;
    }
    public String getIncludesfile() {
        return includesfile;
    }

    public void setIncludesfile(String includesfile) {
        this.includesfile = includesfile;
    }


}