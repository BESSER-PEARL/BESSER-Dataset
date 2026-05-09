





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_UiListenerBinding  {

    private String controlAccess;





    private appBuilderDSL_Action appbuilderdsl_action;




    private appBuilderDSL_InitAction appbuilderdsl_initaction;


    public appBuilderDSL_UiListenerBinding(
        String controlAccess    ) {
        this.controlAccess = controlAccess;
    }


    public String getControlaccess() {
        return controlAccess;
    }

    public void setControlaccess(String controlAccess) {
        this.controlAccess = controlAccess;
    }

    public appBuilderDSL_Action getAppbuilderdsl_action() {
        return appbuilderdsl_action;
    }

    public void setAppbuilderdsl_action(appBuilderDSL_Action appbuilderdsl_action) {
        this.appbuilderdsl_action = appbuilderdsl_action;
    }
    public appBuilderDSL_InitAction getAppbuilderdsl_initaction() {
        return appbuilderdsl_initaction;
    }

    public void setAppbuilderdsl_initaction(appBuilderDSL_InitAction appbuilderdsl_initaction) {
        this.appbuilderdsl_initaction = appbuilderdsl_initaction;
    }

}