





import java.util.List;
import java.util.ArrayList;

public class mathinterpreter_MathExpression  {

    private String description;





    private mathinterpreter_Model mathinterpreter_model;


    public mathinterpreter_MathExpression(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public mathinterpreter_Model getMathinterpreter_model() {
        return mathinterpreter_model;
    }

    public void setMathinterpreter_model(mathinterpreter_Model mathinterpreter_model) {
        this.mathinterpreter_model = mathinterpreter_model;
    }

}