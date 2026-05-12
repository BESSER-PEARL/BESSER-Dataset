





import java.util.List;
import java.util.ArrayList;

public class sml_VariableDeclaration  {

    private String name;





    private sml_Expression sml_expression;




    private sml_VariableAssignment sml_variableassignment;


    public sml_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_Expression getSml_expression() {
        return sml_expression;
    }

    public void setSml_expression(sml_Expression sml_expression) {
        this.sml_expression = sml_expression;
    }
    public sml_VariableAssignment getSml_variableassignment() {
        return sml_variableassignment;
    }

    public void setSml_variableassignment(sml_VariableAssignment sml_variableassignment) {
        this.sml_variableassignment = sml_variableassignment;
    }

}