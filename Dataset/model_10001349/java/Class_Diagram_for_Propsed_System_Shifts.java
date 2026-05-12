





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Shifts  {

    private String starttime;
    private String endtime;
    private String shiftaname;
    private String id;



    public Class_Diagram_for_Propsed_System_Shifts(
        String starttime,        String endtime,        String shiftaname,        String id    ) {
        this.starttime = starttime;
        this.endtime = endtime;
        this.shiftaname = shiftaname;
        this.id = id;
    }


    public String getStarttime() {
        return starttime;
    }

    public void setStarttime(String starttime) {
        this.starttime = starttime;
    }
    public String getEndtime() {
        return endtime;
    }

    public void setEndtime(String endtime) {
        this.endtime = endtime;
    }
    public String getShiftaname() {
        return shiftaname;
    }

    public void setShiftaname(String shiftaname) {
        this.shiftaname = shiftaname;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}