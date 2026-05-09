





import java.util.List;
import java.util.ArrayList;

public class cSharp_StatementExpression  {

    private String assignementOperator;
    private String incrimentDecrement;





    private cSharp_Type csharp_type;




    private cSharp_ArgumentList csharp_argumentlist;




    private cSharp_UnaryExpression csharp_unaryexpression;




    private cSharp_Expression csharp_expression;




    private cSharp_EmbeddedStatement csharp_embeddedstatement;




    private cSharp_PrimaryExpression csharp_primaryexpression;


    public cSharp_StatementExpression(
        String assignementOperator,        String incrimentDecrement    ) {
        this.assignementOperator = assignementOperator;
        this.incrimentDecrement = incrimentDecrement;
    }


    public String getAssignementoperator() {
        return assignementOperator;
    }

    public void setAssignementoperator(String assignementOperator) {
        this.assignementOperator = assignementOperator;
    }
    public String getIncrimentdecrement() {
        return incrimentDecrement;
    }

    public void setIncrimentdecrement(String incrimentDecrement) {
        this.incrimentDecrement = incrimentDecrement;
    }

    public cSharp_Type getCsharp_type() {
        return csharp_type;
    }

    public void setCsharp_type(cSharp_Type csharp_type) {
        this.csharp_type = csharp_type;
    }
    public cSharp_ArgumentList getCsharp_argumentlist() {
        return csharp_argumentlist;
    }

    public void setCsharp_argumentlist(cSharp_ArgumentList csharp_argumentlist) {
        this.csharp_argumentlist = csharp_argumentlist;
    }
    public cSharp_UnaryExpression getCsharp_unaryexpression() {
        return csharp_unaryexpression;
    }

    public void setCsharp_unaryexpression(cSharp_UnaryExpression csharp_unaryexpression) {
        this.csharp_unaryexpression = csharp_unaryexpression;
    }
    public cSharp_Expression getCsharp_expression() {
        return csharp_expression;
    }

    public void setCsharp_expression(cSharp_Expression csharp_expression) {
        this.csharp_expression = csharp_expression;
    }
    public cSharp_EmbeddedStatement getCsharp_embeddedstatement() {
        return csharp_embeddedstatement;
    }

    public void setCsharp_embeddedstatement(cSharp_EmbeddedStatement csharp_embeddedstatement) {
        this.csharp_embeddedstatement = csharp_embeddedstatement;
    }
    public cSharp_PrimaryExpression getCsharp_primaryexpression() {
        return csharp_primaryexpression;
    }

    public void setCsharp_primaryexpression(cSharp_PrimaryExpression csharp_primaryexpression) {
        this.csharp_primaryexpression = csharp_primaryexpression;
    }

}