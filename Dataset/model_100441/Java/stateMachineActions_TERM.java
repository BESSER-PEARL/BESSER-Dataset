





import java.util.List;
import java.util.ArrayList;

public class stateMachineActions_TERM  {

    private int constant;
    private String variable;



    public stateMachineActions_TERM(
        int constant,        String variable    ) {
        this.constant = constant;
        this.variable = variable;
    }


    public int getConstant() {
        return constant;
    }

    public void setConstant(int constant) {
        this.constant = constant;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }


}