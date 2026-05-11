





import java.util.List;
import java.util.ArrayList;

public class mathInterpreter_Variable  {

    private String name;





    private mathInterpreter_Solution mathinterpreter_solution;


    public mathInterpreter_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mathInterpreter_Solution getMathinterpreter_solution() {
        return mathinterpreter_solution;
    }

    public void setMathinterpreter_solution(mathInterpreter_Solution mathinterpreter_solution) {
        this.mathinterpreter_solution = mathinterpreter_solution;
    }

}