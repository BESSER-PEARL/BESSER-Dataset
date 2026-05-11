





import java.util.List;
import java.util.ArrayList;

public class ansic_jump_statement  {

    private String return_vazio;
    private String identifier;
    private String return_;
    private String break_;





    private ansic_expression ansic_expression;




    private ansic_statement ansic_statement;


    public ansic_jump_statement(
        String return_vazio,        String identifier,        String return_,        String break_    ) {
        this.return_vazio = return_vazio;
        this.identifier = identifier;
        this.return_ = return_;
        this.break_ = break_;
    }


    public String getReturn_vazio() {
        return return_vazio;
    }

    public void setReturn_vazio(String return_vazio) {
        this.return_vazio = return_vazio;
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
    public String getBreak_() {
        return break_;
    }

    public void setBreak_(String break_) {
        this.break_ = break_;
    }

    public ansic_expression getAnsic_expression() {
        return ansic_expression;
    }

    public void setAnsic_expression(ansic_expression ansic_expression) {
        this.ansic_expression = ansic_expression;
    }
    public ansic_statement getAnsic_statement() {
        return ansic_statement;
    }

    public void setAnsic_statement(ansic_statement ansic_statement) {
        this.ansic_statement = ansic_statement;
    }

}