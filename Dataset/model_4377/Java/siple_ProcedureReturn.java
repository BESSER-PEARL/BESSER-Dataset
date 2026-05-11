





import java.util.List;
import java.util.ArrayList;

public class siple_ProcedureReturn extends Statement {

    private String Type;





    private siple_Expression siple_expression;


    public siple_ProcedureReturn(
        String Type    ) {
        super(
        );
        this.Type = Type;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public siple_Expression getSiple_expression() {
        return siple_expression;
    }

    public void setSiple_expression(siple_Expression siple_expression) {
        this.siple_expression = siple_expression;
    }

}