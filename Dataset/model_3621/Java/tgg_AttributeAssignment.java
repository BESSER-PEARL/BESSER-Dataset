





import java.util.List;
import java.util.ArrayList;

public class tgg_AttributeAssignment  {

    private String op;





    private tgg_ObjectVariablePattern tgg_objectvariablepattern;




    private tgg_EAttribute tgg_eattribute;




    private tgg_Expression tgg_expression;


    public tgg_AttributeAssignment(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public tgg_ObjectVariablePattern getTgg_objectvariablepattern() {
        return tgg_objectvariablepattern;
    }

    public void setTgg_objectvariablepattern(tgg_ObjectVariablePattern tgg_objectvariablepattern) {
        this.tgg_objectvariablepattern = tgg_objectvariablepattern;
    }
    public tgg_EAttribute getTgg_eattribute() {
        return tgg_eattribute;
    }

    public void setTgg_eattribute(tgg_EAttribute tgg_eattribute) {
        this.tgg_eattribute = tgg_eattribute;
    }
    public tgg_Expression getTgg_expression() {
        return tgg_expression;
    }

    public void setTgg_expression(tgg_Expression tgg_expression) {
        this.tgg_expression = tgg_expression;
    }

}