





import java.util.List;
import java.util.ArrayList;

public class pp1_CollectExpression extends Expression {






    private pp1_Expression pp1_expression;




    private pp1_ICollectQuery pp1_icollectquery;




    private pp1_AttributeOperations pp1_attributeoperations;


    public pp1_CollectExpression(
    ) {
        super(
        );
    }



    public pp1_Expression getPp1_expression() {
        return pp1_expression;
    }

    public void setPp1_expression(pp1_Expression pp1_expression) {
        this.pp1_expression = pp1_expression;
    }
    public pp1_ICollectQuery getPp1_icollectquery() {
        return pp1_icollectquery;
    }

    public void setPp1_icollectquery(pp1_ICollectQuery pp1_icollectquery) {
        this.pp1_icollectquery = pp1_icollectquery;
    }
    public pp1_AttributeOperations getPp1_attributeoperations() {
        return pp1_attributeoperations;
    }

    public void setPp1_attributeoperations(pp1_AttributeOperations pp1_attributeoperations) {
        this.pp1_attributeoperations = pp1_attributeoperations;
    }

}