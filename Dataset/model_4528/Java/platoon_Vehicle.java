





import java.util.List;
import java.util.ArrayList;

public class platoon_Vehicle  {

    private String name;





    private platoon_FV platoon_fv;


    public platoon_Vehicle(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public platoon_FV getPlatoon_fv() {
        return platoon_fv;
    }

    public void setPlatoon_fv(platoon_FV platoon_fv) {
        this.platoon_fv = platoon_fv;
    }

}