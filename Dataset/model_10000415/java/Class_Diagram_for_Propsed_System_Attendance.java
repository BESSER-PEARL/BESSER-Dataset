





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Attendance  {

    private String timein;
    private int empid;
    private int id;
    private String timeout;



    public Class_Diagram_for_Propsed_System_Attendance(
        String timein,        int empid,        int id,        String timeout    ) {
        this.timein = timein;
        this.empid = empid;
        this.id = id;
        this.timeout = timeout;
    }


    public String getTimein() {
        return timein;
    }

    public void setTimein(String timein) {
        this.timein = timein;
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
    public String getTimeout() {
        return timeout;
    }

    public void setTimeout(String timeout) {
        this.timeout = timeout;
    }


}