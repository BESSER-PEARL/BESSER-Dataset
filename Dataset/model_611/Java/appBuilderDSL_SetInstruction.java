





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_SetInstruction extends Instruction {

    private String modelAccess;





    private appBuilderDSL_Attribute appbuilderdsl_attribute;


    public appBuilderDSL_SetInstruction(
        String modelAccess    ) {
        super(
        );
        this.modelAccess = modelAccess;
    }


    public String getModelaccess() {
        return modelAccess;
    }

    public void setModelaccess(String modelAccess) {
        this.modelAccess = modelAccess;
    }

    public appBuilderDSL_Attribute getAppbuilderdsl_attribute() {
        return appbuilderdsl_attribute;
    }

    public void setAppbuilderdsl_attribute(appBuilderDSL_Attribute appbuilderdsl_attribute) {
        this.appbuilderdsl_attribute = appbuilderdsl_attribute;
    }

}