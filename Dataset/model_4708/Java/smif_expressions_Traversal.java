





import java.util.List;
import java.util.ArrayList;

public class smif_expressions_Traversal extends expressions_ExpressionNode, properties_PropertyOwner {

    private String inverse;
    private String traverseToRelation;





    private List<PropertyType> propertytypes;


    public smif_expressions_Traversal(
        String inverse,        String traverseToRelation    ) {
        super(
        );
        this.inverse = inverse;
        this.traverseToRelation = traverseToRelation;
        this.propertytypes = new ArrayList<>();
    }

    public smif_expressions_Traversal(
        String inverse,        String traverseToRelation        ArrayList<PropertyType> propertytypes    ) {
        this.inverse = inverse;
        this.traverseToRelation = traverseToRelation;
        this.propertytypes = propertytypes;
    }

    public String getInverse() {
        return inverse;
    }

    public void setInverse(String inverse) {
        this.inverse = inverse;
    }
    public String getTraversetorelation() {
        return traverseToRelation;
    }

    public void setTraversetorelation(String traverseToRelation) {
        this.traverseToRelation = traverseToRelation;
    }

    public List<PropertyType> getPropertytypes() {
        return propertytypes;
    }

    public void addPropertytype(Propertytype propertytype) {
        this.propertytypes.add(propertytype);
    }

}