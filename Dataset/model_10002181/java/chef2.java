





import java.util.List;
import java.util.ArrayList;

public class chef2  {






    private dayplan dayplan;




    private List<dayplan> dayplans;




    private kitchen_worker kitchen_worker;


    public chef2(
    ) {
        this.dayplans = new ArrayList<>();
    }

    public chef2(
        ArrayList<dayplan> dayplans    ) {
        this.dayplans = dayplans;
    }


    public dayplan getDayplan() {
        return dayplan;
    }

    public void setDayplan(dayplan dayplan) {
        this.dayplan = dayplan;
    }
    public List<dayplan> getDayplans() {
        return dayplans;
    }

    public void addDayplan(Dayplan dayplan) {
        this.dayplans.add(dayplan);
    }
    public kitchen_worker getKitchen_worker() {
        return kitchen_worker;
    }

    public void setKitchen_worker(kitchen_worker kitchen_worker) {
        this.kitchen_worker = kitchen_worker;
    }

}