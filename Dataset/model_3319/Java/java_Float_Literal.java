





import java.util.List;
import java.util.ArrayList;

public class java_Float_Literal  {

    private int decimalDigits1;
    private String exp;
    private String floatTypeSufix;
    private int decimalDigits2;





    private java_Literal_Expression java_literal_expression;


    public java_Float_Literal(
        int decimalDigits1,        String exp,        String floatTypeSufix,        int decimalDigits2    ) {
        this.decimalDigits1 = decimalDigits1;
        this.exp = exp;
        this.floatTypeSufix = floatTypeSufix;
        this.decimalDigits2 = decimalDigits2;
    }


    public int getDecimaldigits1() {
        return decimalDigits1;
    }

    public void setDecimaldigits1(int decimalDigits1) {
        this.decimalDigits1 = decimalDigits1;
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
    public int getDecimaldigits2() {
        return decimalDigits2;
    }

    public void setDecimaldigits2(int decimalDigits2) {
        this.decimalDigits2 = decimalDigits2;
    }

    public java_Literal_Expression getJava_literal_expression() {
        return java_literal_expression;
    }

    public void setJava_literal_expression(java_Literal_Expression java_literal_expression) {
        this.java_literal_expression = java_literal_expression;
    }

}