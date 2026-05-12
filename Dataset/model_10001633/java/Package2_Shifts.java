





import java.util.List;
import java.util.ArrayList;

public class Package2_Shifts  {

    private String endtime;
    private String shiftaname;
    private String starttime;
    private String id;



    public Package2_Shifts(
        String endtime,        String shiftaname,        String starttime,        String id    ) {
        this.endtime = endtime;
        this.shiftaname = shiftaname;
        this.starttime = starttime;
        this.id = id;
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
    public String getStarttime() {
        return starttime;
    }

    public void setStarttime(String starttime) {
        this.starttime = starttime;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}