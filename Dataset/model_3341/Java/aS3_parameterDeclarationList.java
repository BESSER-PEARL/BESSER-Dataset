





import java.util.List;
import java.util.ArrayList;

public class aS3_parameterDeclarationList  {






    private aS3_functionSignature as3_functionsignature;




    private List<aS3_Parameter> as3_parameters;


    public aS3_parameterDeclarationList(
    ) {
        this.as3_parameters = new ArrayList<>();
    }

    public aS3_parameterDeclarationList(
        ArrayList<aS3_Parameter> as3_parameters    ) {
        this.as3_parameters = as3_parameters;
    }


    public aS3_functionSignature getAs3_functionsignature() {
        return as3_functionsignature;
    }

    public void setAs3_functionsignature(aS3_functionSignature as3_functionsignature) {
        this.as3_functionsignature = as3_functionsignature;
    }
    public List<aS3_Parameter> getAs3_parameters() {
        return as3_parameters;
    }

    public void addAs3_parameter(As3_parameter as3_parameter) {
        this.as3_parameters.add(as3_parameter);
    }

}