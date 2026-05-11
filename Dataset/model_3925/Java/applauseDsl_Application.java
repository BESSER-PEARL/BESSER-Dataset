





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Application  {

    private boolean tabbarApplication;
    private String name;





    private applauseDsl_ApplauseModel applausedsl_applausemodel;


    public applauseDsl_Application(
        boolean tabbarApplication,        String name    ) {
        this.tabbarApplication = tabbarApplication;
        this.name = name;
    }


    public boolean getTabbarapplication() {
        return tabbarApplication;
    }

    public void setTabbarapplication(boolean tabbarApplication) {
        this.tabbarApplication = tabbarApplication;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public applauseDsl_ApplauseModel getApplausedsl_applausemodel() {
        return applausedsl_applausemodel;
    }

    public void setApplausedsl_applausemodel(applauseDsl_ApplauseModel applausedsl_applausemodel) {
        this.applausedsl_applausemodel = applausedsl_applausemodel;
    }

}