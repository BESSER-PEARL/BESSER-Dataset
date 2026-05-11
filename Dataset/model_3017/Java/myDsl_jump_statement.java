





import java.util.List;
import java.util.ArrayList;

public class myDsl_jump_statement  {

    private String return_;
    private String break_;
    private String continue_;
    private String goto;
    private String identifier;





    private myDsl_expression mydsl_expression;




    private myDsl_statement mydsl_statement;


    public myDsl_jump_statement(
        String return_,        String break_,        String continue_,        String goto,        String identifier    ) {
        this.return_ = return_;
        this.break_ = break_;
        this.continue_ = continue_;
        this.goto = goto;
        this.identifier = identifier;
    }


    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }
    public String getBreak_() {
        return break_;
    }

    public void setBreak_(String break_) {
        this.break_ = break_;
    }
    public String getContinue_() {
        return continue_;
    }

    public void setContinue_(String continue_) {
        this.continue_ = continue_;
    }
    public String getGoto() {
        return goto;
    }

    public void setGoto(String goto) {
        this.goto = goto;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
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