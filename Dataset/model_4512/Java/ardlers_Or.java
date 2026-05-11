





import java.util.List;
import java.util.ArrayList;

public class ardlers_Or  {

    private String operator;





    private ardlers_Or ardlers_or;




    private ardlers_Rule ardlers_rule;


    public ardlers_Or(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public ardlers_Or getArdlers_or() {
        return ardlers_or;
    }

    public void setArdlers_or(ardlers_Or ardlers_or) {
        this.ardlers_or = ardlers_or;
    }
    public ardlers_Rule getArdlers_rule() {
        return ardlers_rule;
    }

    public void setArdlers_rule(ardlers_Rule ardlers_rule) {
        this.ardlers_rule = ardlers_rule;
    }

}