





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Condition  {

    private String name;





    private appBuilderDSL_ValidationBinding appbuilderdsl_validationbinding;




    private appBuilderDSL_Validator appbuilderdsl_validator;


    public appBuilderDSL_Condition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public appBuilderDSL_ValidationBinding getAppbuilderdsl_validationbinding() {
        return appbuilderdsl_validationbinding;
    }

    public void setAppbuilderdsl_validationbinding(appBuilderDSL_ValidationBinding appbuilderdsl_validationbinding) {
        this.appbuilderdsl_validationbinding = appbuilderdsl_validationbinding;
    }
    public appBuilderDSL_Validator getAppbuilderdsl_validator() {
        return appbuilderdsl_validator;
    }

    public void setAppbuilderdsl_validator(appBuilderDSL_Validator appbuilderdsl_validator) {
        this.appbuilderdsl_validator = appbuilderdsl_validator;
    }

}