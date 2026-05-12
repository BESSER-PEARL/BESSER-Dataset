





import java.util.List;
import java.util.ArrayList;

public class Plan1  {

    private String day_plan;
    private String Monthly_plan;
    private String weekly_plan;





    private List<Kitchen_worker> kitchen_workers;




    private List<chef1> chef1s;




    private Customer1 customer1;


    public Plan1(
        String day_plan,        String Monthly_plan,        String weekly_plan    ) {
        this.day_plan = day_plan;
        this.Monthly_plan = Monthly_plan;
        this.weekly_plan = weekly_plan;
        this.kitchen_workers = new ArrayList<>();
        this.chef1s = new ArrayList<>();
    }

    public Plan1(
        String day_plan,        String Monthly_plan,        String weekly_plan        ArrayList<Kitchen_worker> kitchen_workers,        ArrayList<chef1> chef1s    ) {
        this.day_plan = day_plan;
        this.Monthly_plan = Monthly_plan;
        this.weekly_plan = weekly_plan;
        this.kitchen_workers = kitchen_workers;
        this.chef1s = chef1s;
    }

    public String getDay_plan() {
        return day_plan;
    }

    public void setDay_plan(String day_plan) {
        this.day_plan = day_plan;
    }
    public String getMonthly_plan() {
        return Monthly_plan;
    }

    public void setMonthly_plan(String Monthly_plan) {
        this.Monthly_plan = Monthly_plan;
    }
    public String getWeekly_plan() {
        return weekly_plan;
    }

    public void setWeekly_plan(String weekly_plan) {
        this.weekly_plan = weekly_plan;
    }

    public List<Kitchen_worker> getKitchen_workers() {
        return kitchen_workers;
    }

    public void addKitchen_worker(Kitchen_worker kitchen_worker) {
        this.kitchen_workers.add(kitchen_worker);
    }
    public List<chef1> getChef1s() {
        return chef1s;
    }

    public void addChef1(Chef1 chef1) {
        this.chef1s.add(chef1);
    }
    public Customer1 getCustomer1() {
        return customer1;
    }

    public void setCustomer1(Customer1 customer1) {
        this.customer1 = customer1;
    }

}