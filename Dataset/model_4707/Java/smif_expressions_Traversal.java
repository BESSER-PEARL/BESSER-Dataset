





import java.util.List;
import java.util.ArrayList;

public class smif_expressions_Traversal extends expressions_ExpressionNode, properties_PropertyOwner {

    private String traverseToRelation;
    private String inverse;



    public smif_expressions_Traversal(
        String traverseToRelation,        String inverse    ) {
        super(
        );
        this.traverseToRelation = traverseToRelation;
        this.inverse = inverse;
    }


    public String getTraversetorelation() {
        return traverseToRelation;
    }

    public void setTraversetorelation(String traverseToRelation) {
        this.traverseToRelation = traverseToRelation;
    }
    public String getInverse() {
        return inverse;
    }

    public void setInverse(String inverse) {
        this.inverse = inverse;
    }


}