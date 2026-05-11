





import java.util.List;
import java.util.ArrayList;

public class myDsl_jump_statement  {

    private String identifier;
    private String return_;
    private String return_vazio;
    private String break_;





    private myDsl_expression mydsl_expression;




    private myDsl_statement mydsl_statement;


    public myDsl_jump_statement(
        String identifier,        String return_,        String return_vazio,        String break_    ) {
        this.identifier = identifier;
        this.return_ = return_;
        this.return_vazio = return_vazio;
        this.break_ = break_;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }
    public String getReturn_vazio() {
        return return_vazio;
    }

    public void setReturn_vazio(String return_vazio) {
        this.return_vazio = return_vazio;
    }
    public String getBreak_() {
        return break_;
    }

    public void setBreak_(String break_) {
        this.break_ = break_;
    }

    public myDsl_expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}