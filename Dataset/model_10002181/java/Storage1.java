





import java.util.List;
import java.util.ArrayList;

public class Storage1  {

    private int Component_id;
    private String Component_Name;





    private List<chef1> chef1s;




    private List<Kitchen_worker> kitchen_workers;




    private List<Kitchen_worker> kitchen_workers;


    public Storage1(
        int Component_id,        String Component_Name    ) {
        this.Component_id = Component_id;
        this.Component_Name = Component_Name;
        this.chef1s = new ArrayList<>();
        this.kitchen_workers = new ArrayList<>();
        this.kitchen_workers = new ArrayList<>();
    }

    public Storage1(
        int Component_id,        String Component_Name        ArrayList<chef1> chef1s,        ArrayList<Kitchen_worker> kitchen_workers,        ArrayList<Kitchen_worker> kitchen_workers    ) {
        this.Component_id = Component_id;
        this.Component_Name = Component_Name;
        this.chef1s = chef1s;
        this.kitchen_workers = kitchen_workers;
        this.kitchen_workers = kitchen_workers;
    }

    public int getComponent_id() {
        return Component_id;
    }

    public void setComponent_id(int Component_id) {
        this.Component_id = Component_id;
    }
    public String getComponent_name() {
        return Component_Name;
    }

    public void setComponent_name(String Component_Name) {
        this.Component_Name = Component_Name;
    }

    public List<chef1> getChef1s() {
        return chef1s;
    }

    public void addChef1(Chef1 chef1) {
        this.chef1s.add(chef1);
    }
    public List<Kitchen_worker> getKitchen_workers() {
        return kitchen_workers;
    }

    public void addKitchen_worker(Kitchen_worker kitchen_worker) {
        this.kitchen_workers.add(kitchen_worker);
    }
    public List<Kitchen_worker> getKitchen_workers() {
        return kitchen_workers;
    }

    public void addKitchen_worker(Kitchen_worker kitchen_worker) {
        this.kitchen_workers.add(kitchen_worker);
    }

}