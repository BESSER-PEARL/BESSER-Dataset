





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_DataBinding  {

    private String controlAccess;





    private appBuilderDSL_InitAction appbuilderdsl_initaction;


    public appBuilderDSL_DataBinding(
        String controlAccess    ) {
        this.controlAccess = controlAccess;
    }


    public String getControlaccess() {
        return controlAccess;
    }

    public void setControlaccess(String controlAccess) {
        this.controlAccess = controlAccess;
    }

    public appBuilderDSL_InitAction getAppbuilderdsl_initaction() {
        return appbuilderdsl_initaction;
    }

    public void setAppbuilderdsl_initaction(appBuilderDSL_InitAction appbuilderdsl_initaction) {
        this.appbuilderdsl_initaction = appbuilderdsl_initaction;
    }

}