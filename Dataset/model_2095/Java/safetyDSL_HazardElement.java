





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_HazardElement  {

    private String name;





    private safetyDSL_HazardViewpoint safetydsl_hazardviewpoint;


    public safetyDSL_HazardElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public safetyDSL_HazardViewpoint getSafetydsl_hazardviewpoint() {
        return safetydsl_hazardviewpoint;
    }

    public void setSafetydsl_hazardviewpoint(safetyDSL_HazardViewpoint safetydsl_hazardviewpoint) {
        this.safetydsl_hazardviewpoint = safetydsl_hazardviewpoint;
    }

}