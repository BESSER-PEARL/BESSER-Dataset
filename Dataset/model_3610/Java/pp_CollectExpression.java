





import java.util.List;
import java.util.ArrayList;

public class pp_CollectExpression extends Expression {






    private pp_Expression pp_expression;




    private pp_ICollectQuery pp_icollectquery;




    private pp_AttributeOperations pp_attributeoperations;


    public pp_CollectExpression(
    ) {
        super(
        );
    }



    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }
    public pp_ICollectQuery getPp_icollectquery() {
        return pp_icollectquery;
    }

    public void setPp_icollectquery(pp_ICollectQuery pp_icollectquery) {
        this.pp_icollectquery = pp_icollectquery;
    }
    public pp_AttributeOperations getPp_attributeoperations() {
        return pp_attributeoperations;
    }

    public void setPp_attributeoperations(pp_AttributeOperations pp_attributeoperations) {
        this.pp_attributeoperations = pp_attributeoperations;
    }

}