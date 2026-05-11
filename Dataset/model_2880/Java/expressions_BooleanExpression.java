





import java.util.List;
import java.util.ArrayList;

public class expressions_BooleanExpression  {






    private presentation_expressions_NotExpression presentation_expressions_notexpression;




    private presentation_expressions_AndExpression presentation_expressions_andexpression;




    private presentation_expressions_OrExpression presentation_expressions_orexpression;


    public expressions_BooleanExpression(
    ) {
    }



    public presentation_expressions_NotExpression getPresentation_expressions_notexpression() {
        return presentation_expressions_notexpression;
    }

    public void setPresentation_expressions_notexpression(presentation_expressions_NotExpression presentation_expressions_notexpression) {
        this.presentation_expressions_notexpression = presentation_expressions_notexpression;
    }
    public presentation_expressions_AndExpression getPresentation_expressions_andexpression() {
        return presentation_expressions_andexpression;
    }

    public void setPresentation_expressions_andexpression(presentation_expressions_AndExpression presentation_expressions_andexpression) {
        this.presentation_expressions_andexpression = presentation_expressions_andexpression;
    }
    public presentation_expressions_OrExpression getPresentation_expressions_orexpression() {
        return presentation_expressions_orexpression;
    }

    public void setPresentation_expressions_orexpression(presentation_expressions_OrExpression presentation_expressions_orexpression) {
        this.presentation_expressions_orexpression = presentation_expressions_orexpression;
    }

}