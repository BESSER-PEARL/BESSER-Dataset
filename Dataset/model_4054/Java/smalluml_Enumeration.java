





import java.util.List;
import java.util.ArrayList;

public class smalluml_Enumeration extends Type {

    private String variable;
    private String name;



    public smalluml_Enumeration(
        String variable,        String name    ) {
        super(
        );
        this.variable = variable;
        this.name = name;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}