





import java.util.List;
import java.util.ArrayList;

public class builds_TestResult  {

    private int errorCount;
    private int ignoredCount;
    private int passCount;
    private String duration;
    private int failCount;





    private builds_Build builds_build;




    private builds_Build builds_build;


    public builds_TestResult(
        int errorCount,        int ignoredCount,        int passCount,        String duration,        int failCount    ) {
        this.errorCount = errorCount;
        this.ignoredCount = ignoredCount;
        this.passCount = passCount;
        this.duration = duration;
        this.failCount = failCount;
    }


    public int getErrorcount() {
        return errorCount;
    }

    public void setErrorcount(int errorCount) {
        this.errorCount = errorCount;
    }
    public int getIgnoredcount() {
        return ignoredCount;
    }

    public void setIgnoredcount(int ignoredCount) {
        this.ignoredCount = ignoredCount;
    }
    public int getPasscount() {
        return passCount;
    }

    public void setPasscount(int passCount) {
        this.passCount = passCount;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public int getFailcount() {
        return failCount;
    }

    public void setFailcount(int failCount) {
        this.failCount = failCount;
    }

    public builds_Build getBuilds_build() {
        return builds_build;
    }

    public void setBuilds_build(builds_Build builds_build) {
        this.builds_build = builds_build;
    }
    public builds_Build getBuilds_build() {
        return builds_build;
    }

    public void setBuilds_build(builds_Build builds_build) {
        this.builds_build = builds_build;
    }

}