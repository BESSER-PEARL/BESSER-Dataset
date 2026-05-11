





import java.util.List;
import java.util.ArrayList;

public class myDsl_Float_Literal  {

    private String exp;
    private String floatTypeSufix;
    private int decimalDigits1;
    private int decimalDigits2;





    private myDsl_Literal_Expression mydsl_literal_expression;


    public myDsl_Float_Literal(
        String exp,        String floatTypeSufix,        int decimalDigits1,        int decimalDigits2    ) {
        this.exp = exp;
        this.floatTypeSufix = floatTypeSufix;
        this.decimalDigits1 = decimalDigits1;
        this.decimalDigits2 = decimalDigits2;
    }


    public String getExp() {
        return exp;
    }

    public void setExp(String exp) {
        this.exp = exp;
    }
    public String getFloattypesufix() {
        return floatTypeSufix;
    }

    public void setFloattypesufix(String floatTypeSufix) {
        this.floatTypeSufix = floatTypeSufix;
    }
    public int getDecimaldigits1() {
        return decimalDigits1;
    }

    public void setDecimaldigits1(int decimalDigits1) {
        this.decimalDigits1 = decimalDigits1;
    }
    public int getDecimaldigits2() {
        return decimalDigits2;
    }

    public void setDecimaldigits2(int decimalDigits2) {
        this.decimalDigits2 = decimalDigits2;
    }

    public myDsl_Literal_Expression getMydsl_literal_expression() {
        return mydsl_literal_expression;
    }

    public void setMydsl_literal_expression(myDsl_Literal_Expression mydsl_literal_expression) {
        this.mydsl_literal_expression = mydsl_literal_expression;
    }

}