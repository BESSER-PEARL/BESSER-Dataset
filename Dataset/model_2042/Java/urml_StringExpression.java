





import java.util.List;
import java.util.ArrayList;

public class urml_StringExpression  {

    private String str;





    private urml_LogStatement urml_logstatement;




    private urml_Expression urml_expression;


    public urml_StringExpression(
        String str    ) {
        this.str = str;
    }


    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }

    public urml_LogStatement getUrml_logstatement() {
        return urml_logstatement;
    }

    public void setUrml_logstatement(urml_LogStatement urml_logstatement) {
        this.urml_logstatement = urml_logstatement;
    }
    public urml_Expression getUrml_expression() {
        return urml_expression;
    }

    public void setUrml_expression(urml_Expression urml_expression) {
        this.urml_expression = urml_expression;
    }

}