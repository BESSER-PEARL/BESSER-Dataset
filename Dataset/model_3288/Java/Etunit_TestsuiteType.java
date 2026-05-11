





import java.util.List;
import java.util.ArrayList;

public class Etunit_TestsuiteType  {

    private String disabled;
    private String skipped;
    private String tests;
    private String hostname;
    private String timestamp;
    private String package;
    private String failures;
    private String systemOut;
    private String systemErr;
    private String name;
    private String id;
    private String errors;
    private String time;





    private Etunit_PropertiesType etunit_propertiestype;




    private Etunit_DocumentRoot etunit_documentroot;




    private List<Etunit_TestcaseType> etunit_testcasetypes;


    public Etunit_TestsuiteType(
        String disabled,        String skipped,        String tests,        String hostname,        String timestamp,        String package,        String failures,        String systemOut,        String systemErr,        String name,        String id,        String errors,        String time    ) {
        this.disabled = disabled;
        this.skipped = skipped;
        this.tests = tests;
        this.hostname = hostname;
        this.timestamp = timestamp;
        this.package = package;
        this.failures = failures;
        this.systemOut = systemOut;
        this.systemErr = systemErr;
        this.name = name;
        this.id = id;
        this.errors = errors;
        this.time = time;
        this.etunit_testcasetypes = new ArrayList<>();
    }

    public Etunit_TestsuiteType(
        String disabled,        String skipped,        String tests,        String hostname,        String timestamp,        String package,        String failures,        String systemOut,        String systemErr,        String name,        String id,        String errors,        String time        ArrayList<Etunit_TestcaseType> etunit_testcasetypes    ) {
        this.disabled = disabled;
        this.skipped = skipped;
        this.tests = tests;
        this.hostname = hostname;
        this.timestamp = timestamp;
        this.package = package;
        this.failures = failures;
        this.systemOut = systemOut;
        this.systemErr = systemErr;
        this.name = name;
        this.id = id;
        this.errors = errors;
        this.time = time;
        this.etunit_testcasetypes = etunit_testcasetypes;
    }

    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }
    public String getSkipped() {
        return skipped;
    }

    public void setSkipped(String skipped) {
        this.skipped = skipped;
    }
    public String getTests() {
        return tests;
    }

    public void setTests(String tests) {
        this.tests = tests;
    }
    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getFailures() {
        return failures;
    }

    public void setFailures(String failures) {
        this.failures = failures;
    }
    public String getSystemout() {
        return systemOut;
    }

    public void setSystemout(String systemOut) {
        this.systemOut = systemOut;
    }
    public String getSystemerr() {
        return systemErr;
    }

    public void setSystemerr(String systemErr) {
        this.systemErr = systemErr;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    public Etunit_PropertiesType getEtunit_propertiestype() {
        return etunit_propertiestype;
    }

    public void setEtunit_propertiestype(Etunit_PropertiesType etunit_propertiestype) {
        this.etunit_propertiestype = etunit_propertiestype;
    }
    public Etunit_DocumentRoot getEtunit_documentroot() {
        return etunit_documentroot;
    }

    public void setEtunit_documentroot(Etunit_DocumentRoot etunit_documentroot) {
        this.etunit_documentroot = etunit_documentroot;
    }
    public List<Etunit_TestcaseType> getEtunit_testcasetypes() {
        return etunit_testcasetypes;
    }

    public void addEtunit_testcasetype(Etunit_testcasetype etunit_testcasetype) {
        this.etunit_testcasetypes.add(etunit_testcasetype);
    }

}