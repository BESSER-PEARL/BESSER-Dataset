





import java.util.List;
import java.util.ArrayList;

public class myDsl_shift_expression_complement  {

    private String sleft;
    private String sright;





    private myDsl_relational_expression_linha mydsl_relational_expression_linha;




    private myDsl_shift_expression_linha mydsl_shift_expression_linha;




    private myDsl_additive_expression mydsl_additive_expression;


    public myDsl_shift_expression_complement(
        String sleft,        String sright    ) {
        this.sleft = sleft;
        this.sright = sright;
    }


    public String getSleft() {
        return sleft;
    }

    public void setSleft(String sleft) {
        this.sleft = sleft;
    }
    public String getSright() {
        return sright;
    }

    public void setSright(String sright) {
        this.sright = sright;
    }

    public myDsl_relational_expression_linha getMydsl_relational_expression_linha() {
        return mydsl_relational_expression_linha;
    }

    public void setMydsl_relational_expression_linha(myDsl_relational_expression_linha mydsl_relational_expression_linha) {
        this.mydsl_relational_expression_linha = mydsl_relational_expression_linha;
    }
    public myDsl_shift_expression_linha getMydsl_shift_expression_linha() {
        return mydsl_shift_expression_linha;
    }

    public void setMydsl_shift_expression_linha(myDsl_shift_expression_linha mydsl_shift_expression_linha) {
        this.mydsl_shift_expression_linha = mydsl_shift_expression_linha;
    }
    public myDsl_additive_expression getMydsl_additive_expression() {
        return mydsl_additive_expression;
    }

    public void setMydsl_additive_expression(myDsl_additive_expression mydsl_additive_expression) {
        this.mydsl_additive_expression = mydsl_additive_expression;
    }

}