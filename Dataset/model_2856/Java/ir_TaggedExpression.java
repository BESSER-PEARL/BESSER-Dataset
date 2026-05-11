





import java.util.List;
import java.util.ArrayList;

public class ir_TaggedExpression  {

    private String tag;





    private ir_Connection ir_connection;




    private ir_Declaration ir_declaration;




    private ir_Expression ir_expression;


    public ir_TaggedExpression(
        String tag    ) {
        this.tag = tag;
    }


    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public ir_Connection getIr_connection() {
        return ir_connection;
    }

    public void setIr_connection(ir_Connection ir_connection) {
        this.ir_connection = ir_connection;
    }
    public ir_Declaration getIr_declaration() {
        return ir_declaration;
    }

    public void setIr_declaration(ir_Declaration ir_declaration) {
        this.ir_declaration = ir_declaration;
    }
    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }

}