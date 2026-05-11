





import java.util.List;
import java.util.ArrayList;

public class pp_AttributeOperation  {

    private String key;
    private String op;





    private pp_AttributeOperations pp_attributeoperations;




    private pp_Expression pp_expression;


    public pp_AttributeOperation(
        String key,        String op    ) {
        this.key = key;
        this.op = op;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public pp_AttributeOperations getPp_attributeoperations() {
        return pp_attributeoperations;
    }

    public void setPp_attributeoperations(pp_AttributeOperations pp_attributeoperations) {
        this.pp_attributeoperations = pp_attributeoperations;
    }
    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }

}