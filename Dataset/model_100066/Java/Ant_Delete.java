





import java.util.List;
import java.util.ArrayList;

public class Ant_Delete extends FileTask {

    private String includeEmptyDirs;
    private String excludesfile;
    private String includesfile;
    private String failonerror;
    private String dir;
    private String file;
    private String quiet;
    private String includes;
    private String excludes;
    private String defaultexcludes;
    private String verbose;



    public Ant_Delete(
        String includeEmptyDirs,        String excludesfile,        String includesfile,        String failonerror,        String dir,        String file,        String quiet,        String includes,        String excludes,        String defaultexcludes,        String verbose    ) {
        super(
        );
        this.includeEmptyDirs = includeEmptyDirs;
        this.excludesfile = excludesfile;
        this.includesfile = includesfile;
        this.failonerror = failonerror;
        this.dir = dir;
        this.file = file;
        this.quiet = quiet;
        this.includes = includes;
        this.excludes = excludes;
        this.defaultexcludes = defaultexcludes;
        this.verbose = verbose;
    }


    public String getIncludeemptydirs() {
        return includeEmptyDirs;
    }

    public void setIncludeemptydirs(String includeEmptyDirs) {
        this.includeEmptyDirs = includeEmptyDirs;
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
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
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
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getVerbose() {
        return verbose;
    }

    public void setVerbose(String verbose) {
        this.verbose = verbose;
    }


}