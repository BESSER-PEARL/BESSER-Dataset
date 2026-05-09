





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Control  {






    private appBuilderDSL_DataBinding appbuilderdsl_databinding;




    private appBuilderDSL_ValidationBinding appbuilderdsl_validationbinding;




    private appBuilderDSL_UiListenerBinding appbuilderdsl_uilistenerbinding;


    public appBuilderDSL_Control(
    ) {
    }



    public appBuilderDSL_DataBinding getAppbuilderdsl_databinding() {
        return appbuilderdsl_databinding;
    }

    public void setAppbuilderdsl_databinding(appBuilderDSL_DataBinding appbuilderdsl_databinding) {
        this.appbuilderdsl_databinding = appbuilderdsl_databinding;
    }
    public appBuilderDSL_ValidationBinding getAppbuilderdsl_validationbinding() {
        return appbuilderdsl_validationbinding;
    }

    public void setAppbuilderdsl_validationbinding(appBuilderDSL_ValidationBinding appbuilderdsl_validationbinding) {
        this.appbuilderdsl_validationbinding = appbuilderdsl_validationbinding;
    }
    public appBuilderDSL_UiListenerBinding getAppbuilderdsl_uilistenerbinding() {
        return appbuilderdsl_uilistenerbinding;
    }

    public void setAppbuilderdsl_uilistenerbinding(appBuilderDSL_UiListenerBinding appbuilderdsl_uilistenerbinding) {
        this.appbuilderdsl_uilistenerbinding = appbuilderdsl_uilistenerbinding;
    }

}