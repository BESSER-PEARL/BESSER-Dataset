





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Expression  {

    private String terms;





    private appBuilderDSL_DynamicValue appbuilderdsl_dynamicvalue;


    public appBuilderDSL_Expression(
        String terms    ) {
        this.terms = terms;
    }


    public String getTerms() {
        return terms;
    }

    public void setTerms(String terms) {
        this.terms = terms;
    }

    public appBuilderDSL_DynamicValue getAppbuilderdsl_dynamicvalue() {
        return appbuilderdsl_dynamicvalue;
    }

    public void setAppbuilderdsl_dynamicvalue(appBuilderDSL_DynamicValue appbuilderdsl_dynamicvalue) {
        this.appbuilderdsl_dynamicvalue = appbuilderdsl_dynamicvalue;
    }

}