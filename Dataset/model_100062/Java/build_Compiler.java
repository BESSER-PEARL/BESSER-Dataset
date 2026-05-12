





import java.util.List;
import java.util.ArrayList;

public class build_Compiler  {

    private boolean verbose;
    private String args;
    private boolean debugInfo;
    private String sourceVersion;
    private boolean failOnError;
    private String targetVersion;



    public build_Compiler(
        boolean verbose,        String args,        boolean debugInfo,        String sourceVersion,        boolean failOnError,        String targetVersion    ) {
        this.verbose = verbose;
        this.args = args;
        this.debugInfo = debugInfo;
        this.sourceVersion = sourceVersion;
        this.failOnError = failOnError;
        this.targetVersion = targetVersion;
    }


    public boolean getVerbose() {
        return verbose;
    }

    public void setVerbose(boolean verbose) {
        this.verbose = verbose;
    }
    public String getArgs() {
        return args;
    }

    public void setArgs(String args) {
        this.args = args;
    }
    public boolean getDebuginfo() {
        return debugInfo;
    }

    public void setDebuginfo(boolean debugInfo) {
        this.debugInfo = debugInfo;
    }
    public String getSourceversion() {
        return sourceVersion;
    }

    public void setSourceversion(String sourceVersion) {
        this.sourceVersion = sourceVersion;
    }
    public boolean getFailonerror() {
        return failOnError;
    }

    public void setFailonerror(boolean failOnError) {
        this.failOnError = failOnError;
    }
    public String getTargetversion() {
        return targetVersion;
    }

    public void setTargetversion(String targetVersion) {
        this.targetVersion = targetVersion;
    }


}