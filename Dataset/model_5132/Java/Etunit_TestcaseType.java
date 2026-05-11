





import java.util.List;
import java.util.ArrayList;

public class Etunit_TestcaseType  {

    private String time;
    private String name;
    private String classname;





    private Etunit_ErrorType etunit_errortype;




    private Etunit_Testsuite etunit_testsuite;




    private Etunit_FailureType etunit_failuretype;


    public Etunit_TestcaseType(
        String time,        String name,        String classname    ) {
        this.time = time;
        this.name = name;
        this.classname = classname;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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

    public Etunit_ErrorType getEtunit_errortype() {
        return etunit_errortype;
    }

    public void setEtunit_errortype(Etunit_ErrorType etunit_errortype) {
        this.etunit_errortype = etunit_errortype;
    }
    public Etunit_Testsuite getEtunit_testsuite() {
        return etunit_testsuite;
    }

    public void setEtunit_testsuite(Etunit_Testsuite etunit_testsuite) {
        this.etunit_testsuite = etunit_testsuite;
    }
    public Etunit_FailureType getEtunit_failuretype() {
        return etunit_failuretype;
    }

    public void setEtunit_failuretype(Etunit_FailureType etunit_failuretype) {
        this.etunit_failuretype = etunit_failuretype;
    }

}