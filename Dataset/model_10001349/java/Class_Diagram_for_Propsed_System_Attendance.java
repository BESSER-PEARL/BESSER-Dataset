





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Attendance  {

    private int id;
    private int empid;
    private String timein;
    private String timeout;



    public Class_Diagram_for_Propsed_System_Attendance(
        int id,        int empid,        String timein,        String timeout    ) {
        this.id = id;
        this.empid = empid;
        this.timein = timein;
        this.timeout = timeout;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public String getTimein() {
        return timein;
    }

    public void setTimein(String timein) {
        this.timein = timein;
    }
    public String getTimeout() {
        return timeout;
    }

    public void setTimeout(String timeout) {
        this.timeout = timeout;
    }


}