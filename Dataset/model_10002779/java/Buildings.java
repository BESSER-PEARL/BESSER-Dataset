





import java.util.List;
import java.util.ArrayList;

public class Buildings  {

    private String start_date;
    private String manager_id;
    private int management_id;
    private String end_date;





    private Manager manager;


    public Buildings(
        String start_date,        String manager_id,        int management_id,        String end_date    ) {
        this.start_date = start_date;
        this.manager_id = manager_id;
        this.management_id = management_id;
        this.end_date = end_date;
    }


    public String getStart_date() {
        return start_date;
    }

    public void setStart_date(String start_date) {
        this.start_date = start_date;
    }
    public String getManager_id() {
        return manager_id;
    }

    public void setManager_id(String manager_id) {
        this.manager_id = manager_id;
    }
    public int getManagement_id() {
        return management_id;
    }

    public void setManagement_id(int management_id) {
        this.management_id = management_id;
    }
    public String getEnd_date() {
        return end_date;
    }

    public void setEnd_date(String end_date) {
        this.end_date = end_date;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}