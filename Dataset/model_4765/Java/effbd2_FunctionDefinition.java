





import java.util.List;
import java.util.ArrayList;

public class effbd2_FunctionDefinition  {

    private String transformationDefinition;





    private effbd2_FunctionSpecification effbd2_functionspecification;


    public effbd2_FunctionDefinition(
        String transformationDefinition    ) {
        this.transformationDefinition = transformationDefinition;
    }


    public String getTransformationdefinition() {
        return transformationDefinition;
    }

    public void setTransformationdefinition(String transformationDefinition) {
        this.transformationDefinition = transformationDefinition;
    }

    public effbd2_FunctionSpecification getEffbd2_functionspecification() {
        return effbd2_functionspecification;
    }

    public void setEffbd2_functionspecification(effbd2_FunctionSpecification effbd2_functionspecification) {
        this.effbd2_functionspecification = effbd2_functionspecification;
    }

}