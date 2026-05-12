





import java.util.List;
import java.util.ArrayList;

public class Ant_Delete extends FileTask {

    private String failonerror;
    private String quiet;
    private String defaultexcludes;
    private String excludesfile;
    private String includes;
    private String excludes;
    private String dir;
    private String verbose;
    private String includeEmptyDirs;
    private String includesfile;
    private String file;



    public Ant_Delete(
        String failonerror,        String quiet,        String defaultexcludes,        String excludesfile,        String includes,        String excludes,        String dir,        String verbose,        String includeEmptyDirs,        String includesfile,        String file    ) {
        super(
        );
        this.failonerror = failonerror;
        this.quiet = quiet;
        this.defaultexcludes = defaultexcludes;
        this.excludesfile = excludesfile;
        this.includes = includes;
        this.excludes = excludes;
        this.dir = dir;
        this.verbose = verbose;
        this.includeEmptyDirs = includeEmptyDirs;
        this.includesfile = includesfile;
        this.file = file;
    }


    public String getFailonerror() {
        return failonerror;
    }

    public void setFailonerror(String failonerror) {
        this.failonerror = failonerror;
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
    public String getExcludesfile() {
        return excludesfile;
    }

    public void setExcludesfile(String excludesfile) {
        this.excludesfile = excludesfile;
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
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}