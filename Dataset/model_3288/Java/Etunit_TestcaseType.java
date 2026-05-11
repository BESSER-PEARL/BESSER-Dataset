





import java.util.List;
import java.util.ArrayList;

public class Etunit_TestcaseType  {

    private String name;
    private String classname;
    private String assertions;
    private String systemErr;
    private String systemOut;
    private String status;
    private String time;





    private List<Etunit_ErrorType> etunit_errortypes;




    private Etunit_DocumentRoot etunit_documentroot;




    private List<Etunit_FailureType> etunit_failuretypes;


    public Etunit_TestcaseType(
        String name,        String classname,        String assertions,        String systemErr,        String systemOut,        String status,        String time    ) {
        this.name = name;
        this.classname = classname;
        this.assertions = assertions;
        this.systemErr = systemErr;
        this.systemOut = systemOut;
        this.status = status;
        this.time = time;
        this.etunit_errortypes = new ArrayList<>();
        this.etunit_failuretypes = new ArrayList<>();
    }

    public Etunit_TestcaseType(
        String name,        String classname,        String assertions,        String systemErr,        String systemOut,        String status,        String time        ArrayList<Etunit_ErrorType> etunit_errortypes,        ArrayList<Etunit_FailureType> etunit_failuretypes    ) {
        this.name = name;
        this.classname = classname;
        this.assertions = assertions;
        this.systemErr = systemErr;
        this.systemOut = systemOut;
        this.status = status;
        this.time = time;
        this.etunit_errortypes = etunit_errortypes;
        this.etunit_failuretypes = etunit_failuretypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getAssertions() {
        return assertions;
    }

    public void setAssertions(String assertions) {
        this.assertions = assertions;
    }
    public String getSystemerr() {
        return systemErr;
    }

    public void setSystemerr(String systemErr) {
        this.systemErr = systemErr;
    }
    public String getSystemout() {
        return systemOut;
    }

    public void setSystemout(String systemOut) {
        this.systemOut = systemOut;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public List<Etunit_ErrorType> getEtunit_errortypes() {
        return etunit_errortypes;
    }

    public void addEtunit_errortype(Etunit_errortype etunit_errortype) {
        this.etunit_errortypes.add(etunit_errortype);
    }
    public Etunit_DocumentRoot getEtunit_documentroot() {
        return etunit_documentroot;
    }

    public void setEtunit_documentroot(Etunit_DocumentRoot etunit_documentroot) {
        this.etunit_documentroot = etunit_documentroot;
    }
    public List<Etunit_FailureType> getEtunit_failuretypes() {
        return etunit_failuretypes;
    }

    public void addEtunit_failuretype(Etunit_failuretype etunit_failuretype) {
        this.etunit_failuretypes.add(etunit_failuretype);
    }

}