





import java.util.List;
import java.util.ArrayList;

public class myDsl_CommCase  {

    private String case;
    private String default;





    private myDsl_CommCaseLinha mydsl_commcaselinha;




    private myDsl_Expression mydsl_expression;




    private myDsl_CommClause mydsl_commclause;


    public myDsl_CommCase(
        String case,        String default    ) {
        this.case = case;
        this.default = default;
    }


    public String getCase() {
        return case;
    }

    public void setCase(String case) {
        this.case = case;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public myDsl_CommCaseLinha getMydsl_commcaselinha() {
        return mydsl_commcaselinha;
    }

    public void setMydsl_commcaselinha(myDsl_CommCaseLinha mydsl_commcaselinha) {
        this.mydsl_commcaselinha = mydsl_commcaselinha;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_CommClause getMydsl_commclause() {
        return mydsl_commclause;
    }

    public void setMydsl_commclause(myDsl_CommClause mydsl_commclause) {
        this.mydsl_commclause = mydsl_commclause;
    }

}