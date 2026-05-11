





import java.util.List;
import java.util.ArrayList;

public class pp1_AttributeOperation  {

    private String key;
    private String op;





    private pp1_AttributeOperations pp1_attributeoperations;




    private pp1_Expression pp1_expression;


    public pp1_AttributeOperation(
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

    public pp1_AttributeOperations getPp1_attributeoperations() {
        return pp1_attributeoperations;
    }

    public void setPp1_attributeoperations(pp1_AttributeOperations pp1_attributeoperations) {
        this.pp1_attributeoperations = pp1_attributeoperations;
    }
    public pp1_Expression getPp1_expression() {
        return pp1_expression;
    }

    public void setPp1_expression(pp1_Expression pp1_expression) {
        this.pp1_expression = pp1_expression;
    }

}