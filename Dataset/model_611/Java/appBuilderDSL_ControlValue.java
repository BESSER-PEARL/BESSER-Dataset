





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_ControlValue extends SetInstructionAssignment {

    private String controlAccess;





    private appBuilderDSL_Control appbuilderdsl_control;


    public appBuilderDSL_ControlValue(
        String controlAccess    ) {
        super(
        );
        this.controlAccess = controlAccess;
    }


    public String getControlaccess() {
        return controlAccess;
    }

    public void setControlaccess(String controlAccess) {
        this.controlAccess = controlAccess;
    }

    public appBuilderDSL_Control getAppbuilderdsl_control() {
        return appbuilderdsl_control;
    }

    public void setAppbuilderdsl_control(appBuilderDSL_Control appbuilderdsl_control) {
        this.appbuilderdsl_control = appbuilderdsl_control;
    }

}