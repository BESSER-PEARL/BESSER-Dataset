





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_SafetyViewpoint  {

    private String name;





    private safetyDSL_SafetyFramework safetydsl_safetyframework;


    public safetyDSL_SafetyViewpoint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public safetyDSL_SafetyFramework getSafetydsl_safetyframework() {
        return safetydsl_safetyframework;
    }

    public void setSafetydsl_safetyframework(safetyDSL_SafetyFramework safetydsl_safetyframework) {
        this.safetydsl_safetyframework = safetydsl_safetyframework;
    }

}