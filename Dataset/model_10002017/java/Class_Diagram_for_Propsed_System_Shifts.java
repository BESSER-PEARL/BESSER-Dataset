





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Shifts  {

    private String shiftaname;
    private String endtime;
    private String starttime;
    private int id;



    public Class_Diagram_for_Propsed_System_Shifts(
        String shiftaname,        String endtime,        String starttime,        int id    ) {
        this.shiftaname = shiftaname;
        this.endtime = endtime;
        this.starttime = starttime;
        this.id = id;
    }


    public String getShiftaname() {
        return shiftaname;
    }

    public void setShiftaname(String shiftaname) {
        this.shiftaname = shiftaname;
    }
    public String getEndtime() {
        return endtime;
    }

    public void setEndtime(String endtime) {
        this.endtime = endtime;
    }
    public String getStarttime() {
        return starttime;
    }

    public void setStarttime(String starttime) {
        this.starttime = starttime;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}