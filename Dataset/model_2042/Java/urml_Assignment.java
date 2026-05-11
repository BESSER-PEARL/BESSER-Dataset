





import java.util.List;
import java.util.ArrayList;

public class urml_Assignment extends StatementOperation, Statement {






    private urml_Expression urml_expression;




    private urml_Assignable urml_assignable;


    public urml_Assignment(
    ) {
        super(
        );
    }



    public urml_Expression getUrml_expression() {
        return urml_expression;
    }

    public void setUrml_expression(urml_Expression urml_expression) {
        this.urml_expression = urml_expression;
    }
    public urml_Assignable getUrml_assignable() {
        return urml_assignable;
    }

    public void setUrml_assignable(urml_Assignable urml_assignable) {
        this.urml_assignable = urml_assignable;
    }

}