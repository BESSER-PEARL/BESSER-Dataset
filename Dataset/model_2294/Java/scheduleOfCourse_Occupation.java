





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_Occupation  {

    private int max;
    private int current;





    private scheduleOfCourse_Shift scheduleofcourse_shift;


    public scheduleOfCourse_Occupation(
        int max,        int current    ) {
        this.max = max;
        this.current = current;
    }


    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getCurrent() {
        return current;
    }

    public void setCurrent(int current) {
        this.current = current;
    }

    public scheduleOfCourse_Shift getScheduleofcourse_shift() {
        return scheduleofcourse_shift;
    }

    public void setScheduleofcourse_shift(scheduleOfCourse_Shift scheduleofcourse_shift) {
        this.scheduleofcourse_shift = scheduleofcourse_shift;
    }

}