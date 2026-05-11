





import java.util.List;
import java.util.ArrayList;

public class pp2_AttributeOperation  {

    private String op;
    private String key;





    private pp2_AttributeOperations pp2_attributeoperations;




    private pp2_Expression pp2_expression;


    public pp2_AttributeOperation(
        String op,        String key    ) {
        this.op = op;
        this.key = key;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public pp2_AttributeOperations getPp2_attributeoperations() {
        return pp2_attributeoperations;
    }

    public void setPp2_attributeoperations(pp2_AttributeOperations pp2_attributeoperations) {
        this.pp2_attributeoperations = pp2_attributeoperations;
    }
    public pp2_Expression getPp2_expression() {
        return pp2_expression;
    }

    public void setPp2_expression(pp2_Expression pp2_expression) {
        this.pp2_expression = pp2_expression;
    }

}