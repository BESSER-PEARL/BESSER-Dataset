





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExprSimple  {

    private String symb;





    private myDsl_Expression mydsl_expression;




    private myDsl_Condition mydsl_condition;




    private myDsl_Nill mydsl_nill;




    private myDsl_ABin mydsl_abin;




    private myDsl_Variable mydsl_variable;


    public myDsl_ExprSimple(
        String symb    ) {
        this.symb = symb;
    }


    public String getSymb() {
        return symb;
    }

    public void setSymb(String symb) {
        this.symb = symb;
    }

    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_Condition getMydsl_condition() {
        return mydsl_condition;
    }

    public void setMydsl_condition(myDsl_Condition mydsl_condition) {
        this.mydsl_condition = mydsl_condition;
    }
    public myDsl_Nill getMydsl_nill() {
        return mydsl_nill;
    }

    public void setMydsl_nill(myDsl_Nill mydsl_nill) {
        this.mydsl_nill = mydsl_nill;
    }
    public myDsl_ABin getMydsl_abin() {
        return mydsl_abin;
    }

    public void setMydsl_abin(myDsl_ABin mydsl_abin) {
        this.mydsl_abin = mydsl_abin;
    }
    public myDsl_Variable getMydsl_variable() {
        return mydsl_variable;
    }

    public void setMydsl_variable(myDsl_Variable mydsl_variable) {
        this.mydsl_variable = mydsl_variable;
    }

}