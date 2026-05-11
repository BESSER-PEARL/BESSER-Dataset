





import java.util.List;
import java.util.ArrayList;

public class myDsl_labeled_statement  {

    private String identifier;
    private String case;
    private String default;





    private myDsl_constant_expression mydsl_constant_expression;




    private myDsl_statement mydsl_statement;




    private myDsl_statement mydsl_statement;


    public myDsl_labeled_statement(
        String identifier,        String case,        String default    ) {
        this.identifier = identifier;
        this.case = case;
        this.default = default;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
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

    public myDsl_constant_expression getMydsl_constant_expression() {
        return mydsl_constant_expression;
    }

    public void setMydsl_constant_expression(myDsl_constant_expression mydsl_constant_expression) {
        this.mydsl_constant_expression = mydsl_constant_expression;
    }
    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}