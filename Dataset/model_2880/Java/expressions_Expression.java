





import java.util.List;
import java.util.ArrayList;

public class expressions_Expression  {






    private presentation_expressions_EqualsExpression presentation_expressions_equalsexpression;




    private presentation_expressions_AssignmentExpression presentation_expressions_assignmentexpression;




    private presentation_statements_Assignment presentation_statements_assignment;


    public expressions_Expression(
    ) {
    }



    public presentation_expressions_EqualsExpression getPresentation_expressions_equalsexpression() {
        return presentation_expressions_equalsexpression;
    }

    public void setPresentation_expressions_equalsexpression(presentation_expressions_EqualsExpression presentation_expressions_equalsexpression) {
        this.presentation_expressions_equalsexpression = presentation_expressions_equalsexpression;
    }
    public presentation_expressions_AssignmentExpression getPresentation_expressions_assignmentexpression() {
        return presentation_expressions_assignmentexpression;
    }

    public void setPresentation_expressions_assignmentexpression(presentation_expressions_AssignmentExpression presentation_expressions_assignmentexpression) {
        this.presentation_expressions_assignmentexpression = presentation_expressions_assignmentexpression;
    }
    public presentation_statements_Assignment getPresentation_statements_assignment() {
        return presentation_statements_assignment;
    }

    public void setPresentation_statements_assignment(presentation_statements_Assignment presentation_statements_assignment) {
        this.presentation_statements_assignment = presentation_statements_assignment;
    }

}