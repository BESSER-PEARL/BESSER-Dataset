





import java.util.List;
import java.util.ArrayList;

public class myDsl_Ampersand_Rule  {

    private String a2;
    private String a1;





    private myDsl_Expression_aux mydsl_expression_aux;


    public myDsl_Ampersand_Rule(
        String a2,        String a1    ) {
        this.a2 = a2;
        this.a1 = a1;
    }


    public String getA2() {
        return a2;
    }

    public void setA2(String a2) {
        this.a2 = a2;
    }
    public String getA1() {
        return a1;
    }

    public void setA1(String a1) {
        this.a1 = a1;
    }

    public myDsl_Expression_aux getMydsl_expression_aux() {
        return mydsl_expression_aux;
    }

    public void setMydsl_expression_aux(myDsl_Expression_aux mydsl_expression_aux) {
        this.mydsl_expression_aux = mydsl_expression_aux;
    }

}