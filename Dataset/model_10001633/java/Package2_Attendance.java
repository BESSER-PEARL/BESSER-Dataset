





import java.util.List;
import java.util.ArrayList;

public class Package2_Attendance  {

    private int empid;
    private String timein;
    private String timeout;
    private int id;



    public Package2_Attendance(
        int empid,        String timein,        String timeout,        int id    ) {
        this.empid = empid;
        this.timein = timein;
        this.timeout = timeout;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}