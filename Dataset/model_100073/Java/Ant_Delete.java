





import java.util.List;
import java.util.ArrayList;

public class Ant_Delete extends FileTask {

    private String verbose;
    private String defaultexcludes;
    private String includes;
    private String failonerror;
    private String excludes;
    private String quiet;
    private String dir;
    private String excludesfile;
    private String includesfile;
    private String includeEmptyDirs;
    private String file;



    public Ant_Delete(
        String verbose,        String defaultexcludes,        String includes,        String failonerror,        String excludes,        String quiet,        String dir,        String excludesfile,        String includesfile,        String includeEmptyDirs,        String file    ) {
        super(
        );
        this.verbose = verbose;
        this.defaultexcludes = defaultexcludes;
        this.includes = includes;
        this.failonerror = failonerror;
        this.excludes = excludes;
        this.quiet = quiet;
        this.dir = dir;
        this.excludesfile = excludesfile;
        this.includesfile = includesfile;
        this.includeEmptyDirs = includeEmptyDirs;
        this.file = file;
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
    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
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
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}