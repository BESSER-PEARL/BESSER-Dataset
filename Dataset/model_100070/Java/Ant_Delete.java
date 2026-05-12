





import java.util.List;
import java.util.ArrayList;

public class Ant_Delete extends FileTask {

    private String dir;
    private String quiet;
    private String includes;
    private String excludes;
    private String verbose;
    private String defaultexcludes;
    private String excludesfile;
    private String includesfile;
    private String includeEmptyDirs;
    private String failonerror;
    private String file;



    public Ant_Delete(
        String dir,        String quiet,        String includes,        String excludes,        String verbose,        String defaultexcludes,        String excludesfile,        String includesfile,        String includeEmptyDirs,        String failonerror,        String file    ) {
        super(
        );
        this.dir = dir;
        this.quiet = quiet;
        this.includes = includes;
        this.excludes = excludes;
        this.verbose = verbose;
        this.defaultexcludes = defaultexcludes;
        this.excludesfile = excludesfile;
        this.includesfile = includesfile;
        this.includeEmptyDirs = includeEmptyDirs;
        this.failonerror = failonerror;
        this.file = file;
    }


    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
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
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
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
    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
    }
    public String getFailonerror() {
        return failonerror;
    }

    public void setFailonerror(String failonerror) {
        this.failonerror = failonerror;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}