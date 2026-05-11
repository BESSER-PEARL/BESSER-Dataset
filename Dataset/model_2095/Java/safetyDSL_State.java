





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_State  {

    private String name;





    private safetyDSL_SafetyCritical safetydsl_safetycritical;


    public safetyDSL_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public safetyDSL_SafetyCritical getSafetydsl_safetycritical() {
        return safetydsl_safetycritical;
    }

    public void setSafetydsl_safetycritical(safetyDSL_SafetyCritical safetydsl_safetycritical) {
        this.safetydsl_safetycritical = safetydsl_safetycritical;
    }

}