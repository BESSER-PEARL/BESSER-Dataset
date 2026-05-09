





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Navigate extends Instruction {

    private String params;





    private appBuilderDSL_Screen appbuilderdsl_screen;


    public appBuilderDSL_Navigate(
        String params    ) {
        super(
        );
        this.params = params;
    }


    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }

    public appBuilderDSL_Screen getAppbuilderdsl_screen() {
        return appbuilderdsl_screen;
    }

    public void setAppbuilderdsl_screen(appBuilderDSL_Screen appbuilderdsl_screen) {
        this.appbuilderdsl_screen = appbuilderdsl_screen;
    }

}