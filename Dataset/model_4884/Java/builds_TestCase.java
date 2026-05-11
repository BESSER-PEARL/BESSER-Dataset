





import java.util.List;
import java.util.ArrayList;

public class builds_TestCase extends TestElement {

    private String message;
    private boolean skipped;
    private String status;
    private String stackTrace;
    private String className;



    public builds_TestCase(
        String message,        boolean skipped,        String status,        String stackTrace,        String className    ) {
        super(
        );
        this.message = message;
        this.skipped = skipped;
        this.status = status;
        this.stackTrace = stackTrace;
        this.className = className;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public boolean getSkipped() {
        return skipped;
    }

    public void setSkipped(boolean skipped) {
        this.skipped = skipped;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getStacktrace() {
        return stackTrace;
    }

    public void setStacktrace(String stackTrace) {
        this.stackTrace = stackTrace;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }


}