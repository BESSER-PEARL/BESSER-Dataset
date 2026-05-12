





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String management_id;
    private String manager_id;



    public Manager(
        String management_id,        String manager_id    ) {
        this.management_id = management_id;
        this.manager_id = manager_id;
    }


    public String getManagement_id() {
        return management_id;
    }

    public void setManagement_id(String management_id) {
        this.management_id = management_id;
    }
    public String getManager_id() {
        return manager_id;
    }

    public void setManager_id(String manager_id) {
        this.manager_id = manager_id;
    }


}