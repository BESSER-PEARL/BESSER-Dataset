





import java.util.List;
import java.util.ArrayList;

public class builds_TestCase extends TestElement {

    private String message;
    private String stackTrace;
    private String status;
    private String className;
    private boolean skipped;





    private builds_TestSuite builds_testsuite;




    private builds_TestSuite builds_testsuite;


    public builds_TestCase(
        String message,        String stackTrace,        String status,        String className,        boolean skipped    ) {
        super(
        );
        this.message = message;
        this.stackTrace = stackTrace;
        this.status = status;
        this.className = className;
        this.skipped = skipped;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getStacktrace() {
        return stackTrace;
    }

    public void setStacktrace(String stackTrace) {
        this.stackTrace = stackTrace;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public boolean getSkipped() {
        return skipped;
    }

    public void setSkipped(boolean skipped) {
        this.skipped = skipped;
    }

    public builds_TestSuite getBuilds_testsuite() {
        return builds_testsuite;
    }

    public void setBuilds_testsuite(builds_TestSuite builds_testsuite) {
        this.builds_testsuite = builds_testsuite;
    }
    public builds_TestSuite getBuilds_testsuite() {
        return builds_testsuite;
    }

    public void setBuilds_testsuite(builds_TestSuite builds_testsuite) {
        this.builds_testsuite = builds_testsuite;
    }

}