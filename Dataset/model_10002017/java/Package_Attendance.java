





import java.util.List;
import java.util.ArrayList;

public class Package_Attendance  {

    private String timein;
    private int empid;
    private String timeout;
    private int id;



    public Package_Attendance(
        String timein,        int empid,        String timeout,        int id    ) {
        this.timein = timein;
        this.empid = empid;
        this.timeout = timeout;
        this.id = id;
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