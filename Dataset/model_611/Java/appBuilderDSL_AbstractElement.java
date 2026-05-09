





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_AbstractElement  {

    private String name;





    private appBuilderDSL_AppBuilder appbuilderdsl_appbuilder;


    public appBuilderDSL_AbstractElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public appBuilderDSL_AppBuilder getAppbuilderdsl_appbuilder() {
        return appbuilderdsl_appbuilder;
    }

    public void setAppbuilderdsl_appbuilder(appBuilderDSL_AppBuilder appbuilderdsl_appbuilder) {
        this.appbuilderdsl_appbuilder = appbuilderdsl_appbuilder;
    }

}