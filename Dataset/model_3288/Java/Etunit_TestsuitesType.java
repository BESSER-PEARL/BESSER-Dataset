





import java.util.List;
import java.util.ArrayList;

public class Etunit_TestsuitesType  {

    private String name;
    private String failures;
    private String errors;
    private String time;
    private String disabled;
    private String tests;





    private List<Etunit_TestsuiteType> etunit_testsuitetypes;




    private Etunit_DocumentRoot etunit_documentroot;


    public Etunit_TestsuitesType(
        String name,        String failures,        String errors,        String time,        String disabled,        String tests    ) {
        this.name = name;
        this.failures = failures;
        this.errors = errors;
        this.time = time;
        this.disabled = disabled;
        this.tests = tests;
        this.etunit_testsuitetypes = new ArrayList<>();
    }

    public Etunit_TestsuitesType(
        String name,        String failures,        String errors,        String time,        String disabled,        String tests        ArrayList<Etunit_TestsuiteType> etunit_testsuitetypes    ) {
        this.name = name;
        this.failures = failures;
        this.errors = errors;
        this.time = time;
        this.disabled = disabled;
        this.tests = tests;
        this.etunit_testsuitetypes = etunit_testsuitetypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }
    public String getTests() {
        return tests;
    }

    public void setTests(String tests) {
        this.tests = tests;
    }

    public List<Etunit_TestsuiteType> getEtunit_testsuitetypes() {
        return etunit_testsuitetypes;
    }

    public void addEtunit_testsuitetype(Etunit_testsuitetype etunit_testsuitetype) {
        this.etunit_testsuitetypes.add(etunit_testsuitetype);
    }
    public Etunit_DocumentRoot getEtunit_documentroot() {
        return etunit_documentroot;
    }

    public void setEtunit_documentroot(Etunit_DocumentRoot etunit_documentroot) {
        this.etunit_documentroot = etunit_documentroot;
    }

}