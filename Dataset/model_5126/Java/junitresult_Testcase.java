





import java.util.List;
import java.util.ArrayList;

public class junitresult_Testcase  {

    private float time;
    private String assertions;
    private String system_err;
    private String system_out;
    private String classname;
    private String status;
    private String name;





    private junitresult_Testsuite junitresult_testsuite;


    public junitresult_Testcase(
        float time,        String assertions,        String system_err,        String system_out,        String classname,        String status,        String name    ) {
        this.time = time;
        this.assertions = assertions;
        this.system_err = system_err;
        this.system_out = system_out;
        this.classname = classname;
        this.status = status;
        this.name = name;
    }


    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
    }
    public String getAssertions() {
        return assertions;
    }

    public void setAssertions(String assertions) {
        this.assertions = assertions;
    }
    public String getSystem_err() {
        return system_err;
    }

    public void setSystem_err(String system_err) {
        this.system_err = system_err;
    }
    public String getSystem_out() {
        return system_out;
    }

    public void setSystem_out(String system_out) {
        this.system_out = system_out;
    }
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public junitresult_Testsuite getJunitresult_testsuite() {
        return junitresult_testsuite;
    }

    public void setJunitresult_testsuite(junitresult_Testsuite junitresult_testsuite) {
        this.junitresult_testsuite = junitresult_testsuite;
    }

}