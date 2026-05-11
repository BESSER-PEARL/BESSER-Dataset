





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_ArchitecturalElement  {

    private String name;





    private safetyDSL_SafetyCriticalViewpoint safetydsl_safetycriticalviewpoint;


    public safetyDSL_ArchitecturalElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public safetyDSL_SafetyCriticalViewpoint getSafetydsl_safetycriticalviewpoint() {
        return safetydsl_safetycriticalviewpoint;
    }

    public void setSafetydsl_safetycriticalviewpoint(safetyDSL_SafetyCriticalViewpoint safetydsl_safetycriticalviewpoint) {
        this.safetydsl_safetycriticalviewpoint = safetydsl_safetycriticalviewpoint;
    }

}