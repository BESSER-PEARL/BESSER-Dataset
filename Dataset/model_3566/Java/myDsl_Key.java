





import java.util.List;
import java.util.ArrayList;

public class myDsl_Key  {






    private myDsl_Expression mydsl_expression;




    private myDsl_KeyedElement mydsl_keyedelement;




    private myDsl_LiteralValue mydsl_literalvalue;


    public myDsl_Key(
    ) {
    }



    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_KeyedElement getMydsl_keyedelement() {
        return mydsl_keyedelement;
    }

    public void setMydsl_keyedelement(myDsl_KeyedElement mydsl_keyedelement) {
        this.mydsl_keyedelement = mydsl_keyedelement;
    }
    public myDsl_LiteralValue getMydsl_literalvalue() {
        return mydsl_literalvalue;
    }

    public void setMydsl_literalvalue(myDsl_LiteralValue mydsl_literalvalue) {
        this.mydsl_literalvalue = mydsl_literalvalue;
    }

}