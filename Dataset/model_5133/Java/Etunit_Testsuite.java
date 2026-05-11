





import java.util.List;
import java.util.ArrayList;

public class Etunit_Testsuite  {

    private String tests;
    private String time;
    private String timestamp;
    private String failures;
    private String name;
    private String skipped;
    private String errors;





    private Etunit_DocumentRoot etunit_documentroot;


    public Etunit_Testsuite(
        String tests,        String time,        String timestamp,        String failures,        String name,        String skipped,        String errors    ) {
        this.tests = tests;
        this.time = time;
        this.timestamp = timestamp;
        this.failures = failures;
        this.name = name;
        this.skipped = skipped;
        this.errors = errors;
    }


    public String getTests() {
        return tests;
    }

    public void setTests(String tests) {
        this.tests = tests;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSkipped() {
        return skipped;
    }

    public void setSkipped(String skipped) {
        this.skipped = skipped;
    }
    public String getErrors() {
        return errors;
    }

    public void setErrors(String errors) {
        this.errors = errors;
    }

    public Etunit_DocumentRoot getEtunit_documentroot() {
        return etunit_documentroot;
    }

    public void setEtunit_documentroot(Etunit_DocumentRoot etunit_documentroot) {
        this.etunit_documentroot = etunit_documentroot;
    }

}