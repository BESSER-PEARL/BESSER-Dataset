





import java.util.List;
import java.util.ArrayList;

public class whileComp_Read  {

    private String variable;





    private whileComp_Definition whilecomp_definition;


    public whileComp_Read(
        String variable    ) {
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public whileComp_Definition getWhilecomp_definition() {
        return whilecomp_definition;
    }

    public void setWhilecomp_definition(whileComp_Definition whilecomp_definition) {
        this.whilecomp_definition = whilecomp_definition;
    }

}