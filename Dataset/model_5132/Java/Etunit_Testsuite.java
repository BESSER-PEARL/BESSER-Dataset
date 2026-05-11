





import java.util.List;
import java.util.ArrayList;

public class Etunit_Testsuite  {

    private String timestamp;
    private String failures;
    private String errors;
    private String time;
    private String tests;
    private String skipped;
    private String name;





    private Etunit_DocumentRoot etunit_documentroot;


    public Etunit_Testsuite(
        String timestamp,        String failures,        String errors,        String time,        String tests,        String skipped,        String name    ) {
        this.timestamp = timestamp;
        this.failures = failures;
        this.errors = errors;
        this.time = time;
        this.tests = tests;
        this.skipped = skipped;
        this.name = name;
    }


    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getFailures() {
        return failures;
    }

    public void setFailures(String failures) {
        this.failures = failures;
    }
    public String getErrors() {
        return errors;
    }

    public void setErrors(String errors) {
        this.errors = errors;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getTests() {
        return tests;
    }

    public void setTests(String tests) {
        this.tests = tests;
    }
    public String getSkipped() {
        return skipped;
    }

    public void setSkipped(String skipped) {
        this.skipped = skipped;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Etunit_DocumentRoot getEtunit_documentroot() {
        return etunit_documentroot;
    }

    public void setEtunit_documentroot(Etunit_DocumentRoot etunit_documentroot) {
        this.etunit_documentroot = etunit_documentroot;
    }

}