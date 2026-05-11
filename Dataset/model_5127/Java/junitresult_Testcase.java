





import java.util.List;
import java.util.ArrayList;

public class junitresult_Testcase  {

    private float time;
    private String classname;
    private String status;
    private String assertions;
    private String system_err;
    private String name;
    private String system_out;



    public junitresult_Testcase(
        float time,        String classname,        String status,        String assertions,        String system_err,        String name,        String system_out    ) {
        this.time = time;
        this.classname = classname;
        this.status = status;
        this.assertions = assertions;
        this.system_err = system_err;
        this.name = name;
        this.system_out = system_out;
    }


    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSystem_out() {
        return system_out;
    }

    public void setSystem_out(String system_out) {
        this.system_out = system_out;
    }


}