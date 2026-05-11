





import java.util.List;
import java.util.ArrayList;

public class transformation_VariableDefinition  {

    private String name;





    private transformation_VariableUse transformation_variableuse;




    private transformation_Lambda transformation_lambda;


    public transformation_VariableDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public transformation_VariableUse getTransformation_variableuse() {
        return transformation_variableuse;
    }

    public void setTransformation_variableuse(transformation_VariableUse transformation_variableuse) {
        this.transformation_variableuse = transformation_variableuse;
    }
    public transformation_Lambda getTransformation_lambda() {
        return transformation_lambda;
    }

    public void setTransformation_lambda(transformation_Lambda transformation_lambda) {
        this.transformation_lambda = transformation_lambda;
    }

}