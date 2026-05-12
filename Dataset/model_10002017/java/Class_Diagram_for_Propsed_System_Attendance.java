





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Attendance  {

    private String timeout;
    private int empid;
    private int id;
    private String timein;



    public Class_Diagram_for_Propsed_System_Attendance(
        String timeout,        int empid,        int id,        String timein    ) {
        this.timeout = timeout;
        this.empid = empid;
        this.id = id;
        this.timein = timein;
    }


    public String getTimeout() {
        return timeout;
    }

    public void setTimeout(String timeout) {
        this.timeout = timeout;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getTimein() {
        return timein;
    }

    public void setTimein(String timein) {
        this.timein = timein;
    }


}