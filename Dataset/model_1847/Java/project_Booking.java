





import java.util.List;
import java.util.ArrayList;

public class project_Booking  {

    private int overtime;
    private int sloppy;



    public project_Booking(
        int overtime,        int sloppy    ) {
        this.overtime = overtime;
        this.sloppy = sloppy;
    }


    public int getOvertime() {
        return overtime;
    }

    public void setOvertime(int overtime) {
        this.overtime = overtime;
    }
    public int getSloppy() {
        return sloppy;
    }

    public void setSloppy(int sloppy) {
        this.sloppy = sloppy;
    }


}