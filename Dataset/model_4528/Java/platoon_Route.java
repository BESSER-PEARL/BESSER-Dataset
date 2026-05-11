





import java.util.List;
import java.util.ArrayList;

public class platoon_Route  {

    private String name;





    private platoon_Model platoon_model;


    public platoon_Route(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public platoon_Model getPlatoon_model() {
        return platoon_model;
    }

    public void setPlatoon_model(platoon_Model platoon_model) {
        this.platoon_model = platoon_model;
    }

}