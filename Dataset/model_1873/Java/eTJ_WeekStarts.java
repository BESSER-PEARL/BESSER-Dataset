





import java.util.List;
import java.util.ArrayList;

public class eTJ_WeekStarts extends ProjectAttribute {

    private boolean sunday;
    private boolean monday;



    public eTJ_WeekStarts(
        boolean sunday,        boolean monday    ) {
        super(
        );
        this.sunday = sunday;
        this.monday = monday;
    }


    public boolean getSunday() {
        return sunday;
    }

    public void setSunday(boolean sunday) {
        this.sunday = sunday;
    }
    public boolean getMonday() {
        return monday;
    }

    public void setMonday(boolean monday) {
        this.monday = monday;
    }


}