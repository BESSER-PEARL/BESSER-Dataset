





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Attribute  {

    private String type;
    private String name;





    private appBuilderDSL_EntryParameters appbuilderdsl_entryparameters;




    private appBuilderDSL_Model appbuilderdsl_model;


    public appBuilderDSL_Attribute(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public appBuilderDSL_EntryParameters getAppbuilderdsl_entryparameters() {
        return appbuilderdsl_entryparameters;
    }

    public void setAppbuilderdsl_entryparameters(appBuilderDSL_EntryParameters appbuilderdsl_entryparameters) {
        this.appbuilderdsl_entryparameters = appbuilderdsl_entryparameters;
    }
    public appBuilderDSL_Model getAppbuilderdsl_model() {
        return appbuilderdsl_model;
    }

    public void setAppbuilderdsl_model(appBuilderDSL_Model appbuilderdsl_model) {
        this.appbuilderdsl_model = appbuilderdsl_model;
    }

}