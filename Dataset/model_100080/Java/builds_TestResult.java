





import java.util.List;
import java.util.ArrayList;

public class builds_TestResult  {

    private int failCount;
    private int ignoredCount;
    private String duration;
    private int errorCount;
    private int passCount;



    public builds_TestResult(
        int failCount,        int ignoredCount,        String duration,        int errorCount,        int passCount    ) {
        this.failCount = failCount;
        this.ignoredCount = ignoredCount;
        this.duration = duration;
        this.errorCount = errorCount;
        this.passCount = passCount;
    }


    public int getFailcount() {
        return failCount;
    }

    public void setFailcount(int failCount) {
        this.failCount = failCount;
    }
    public int getIgnoredcount() {
        return ignoredCount;
    }

    public void setIgnoredcount(int ignoredCount) {
        this.ignoredCount = ignoredCount;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public int getErrorcount() {
        return errorCount;
    }

    public void setErrorcount(int errorCount) {
        this.errorCount = errorCount;
    }
    public int getPasscount() {
        return passCount;
    }

    public void setPasscount(int passCount) {
        this.passCount = passCount;
    }


}