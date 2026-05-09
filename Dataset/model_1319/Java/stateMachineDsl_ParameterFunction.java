





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_ParameterFunction  {

    private String name;





    private stateMachineDsl_ExtDeclaration statemachinedsl_extdeclaration;


    public stateMachineDsl_ParameterFunction(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachineDsl_ExtDeclaration getStatemachinedsl_extdeclaration() {
        return statemachinedsl_extdeclaration;
    }

    public void setStatemachinedsl_extdeclaration(stateMachineDsl_ExtDeclaration statemachinedsl_extdeclaration) {
        this.statemachinedsl_extdeclaration = statemachinedsl_extdeclaration;
    }

}