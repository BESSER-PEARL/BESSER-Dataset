





import java.util.List;
import java.util.ArrayList;

public class sml_Variable  {

    private String name;





    private sml_VariableValue sml_variablevalue;




    private sml_FeatureAccess sml_featureaccess;


    public sml_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_VariableValue getSml_variablevalue() {
        return sml_variablevalue;
    }

    public void setSml_variablevalue(sml_VariableValue sml_variablevalue) {
        this.sml_variablevalue = sml_variablevalue;
    }
    public sml_FeatureAccess getSml_featureaccess() {
        return sml_featureaccess;
    }

    public void setSml_featureaccess(sml_FeatureAccess sml_featureaccess) {
        this.sml_featureaccess = sml_featureaccess;
    }

}