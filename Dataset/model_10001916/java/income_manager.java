





import java.util.List;
import java.util.ArrayList;

public class income_manager  {

    private None manager_id;
    private String manager_name;
    private None duty_hours;



    public income_manager(
        None manager_id,        String manager_name,        None duty_hours    ) {
        this.manager_id = manager_id;
        this.manager_name = manager_name;
        this.duty_hours = duty_hours;
    }


    public None getManager_id() {
        return manager_id;
    }

    public void setManager_id(None manager_id) {
        this.manager_id = manager_id;
    }
    public String getManager_name() {
        return manager_name;
    }

    public void setManager_name(String manager_name) {
        this.manager_name = manager_name;
    }
    public None getDuty_hours() {
        return duty_hours;
    }

    public void setDuty_hours(None duty_hours) {
        this.duty_hours = duty_hours;
    }


}