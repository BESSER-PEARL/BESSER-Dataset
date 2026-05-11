





import java.util.List;
import java.util.ArrayList;

public class builds_TestResult  {

    private String duration;
    private int ignoredCount;
    private int passCount;
    private int errorCount;
    private int failCount;



    public builds_TestResult(
        String duration,        int ignoredCount,        int passCount,        int errorCount,        int failCount    ) {
        this.duration = duration;
        this.ignoredCount = ignoredCount;
        this.passCount = passCount;
        this.errorCount = errorCount;
        this.failCount = failCount;
    }


    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
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
    public int getErrorcount() {
        return errorCount;
    }

    public void setErrorcount(int errorCount) {
        this.errorCount = errorCount;
    }
    public int getFailcount() {
        return failCount;
    }

    public void setFailcount(int failCount) {
        this.failCount = failCount;
    }


}