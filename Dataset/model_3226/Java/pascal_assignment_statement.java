





import java.util.List;
import java.util.ArrayList;

public class pascal_assignment_statement extends simple_statement {

    private String identifier;
    private String variable;



    public pascal_assignment_statement(
        String identifier,        String variable    ) {
        super(
        );
        this.identifier = identifier;
        this.variable = variable;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }


}