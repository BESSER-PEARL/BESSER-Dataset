





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Screen  {

    private String name;





    private appBuilderDSL_Ui appbuilderdsl_ui;




    private appBuilderDSL_Main appbuilderdsl_main;


    public appBuilderDSL_Screen(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public appBuilderDSL_Ui getAppbuilderdsl_ui() {
        return appbuilderdsl_ui;
    }

    public void setAppbuilderdsl_ui(appBuilderDSL_Ui appbuilderdsl_ui) {
        this.appbuilderdsl_ui = appbuilderdsl_ui;
    }
    public appBuilderDSL_Main getAppbuilderdsl_main() {
        return appbuilderdsl_main;
    }

    public void setAppbuilderdsl_main(appBuilderDSL_Main appbuilderdsl_main) {
        this.appbuilderdsl_main = appbuilderdsl_main;
    }

}