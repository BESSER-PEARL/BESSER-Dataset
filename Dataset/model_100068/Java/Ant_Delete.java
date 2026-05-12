





import java.util.List;
import java.util.ArrayList;

public class Ant_Delete extends FileTask {

    private String includes;
    private String excludesfile;
    private String includesfile;
    private String defaultexcludes;
    private String includeEmptyDirs;
    private String dir;
    private String verbose;
    private String quiet;
    private String failonerror;
    private String excludes;
    private String file;



    public Ant_Delete(
        String includes,        String excludesfile,        String includesfile,        String defaultexcludes,        String includeEmptyDirs,        String dir,        String verbose,        String quiet,        String failonerror,        String excludes,        String file    ) {
        super(
        );
        this.includes = includes;
        this.excludesfile = excludesfile;
        this.includesfile = includesfile;
        this.defaultexcludes = defaultexcludes;
        this.includeEmptyDirs = includeEmptyDirs;
        this.dir = dir;
        this.verbose = verbose;
        this.quiet = quiet;
        this.failonerror = failonerror;
        this.excludes = excludes;
        this.file = file;
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
    public String getVerbose() {
        return verbose;
    }

    public void setVerbose(String verbose) {
        this.verbose = verbose;
    }
    public String getQuiet() {
        return quiet;
    }

    public void setQuiet(String quiet) {
        this.quiet = quiet;
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
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}