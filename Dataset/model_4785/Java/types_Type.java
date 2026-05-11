





import java.util.List;
import java.util.ArrayList;

public class types_Type extends PackageMember {






    private types_TypedElement types_typedelement;




    private types_TypedElement types_typedelement;




    private List<types_TypeConstraint> types_typeconstraints;


    public types_Type(
    ) {
        super(
        );
        this.types_typeconstraints = new ArrayList<>();
    }

    public types_Type(
        ArrayList<types_TypeConstraint> types_typeconstraints    ) {
        this.types_typeconstraints = types_typeconstraints;
    }


    public types_TypedElement getTypes_typedelement() {
        return types_typedelement;
    }

    public void setTypes_typedelement(types_TypedElement types_typedelement) {
        this.types_typedelement = types_typedelement;
    }
    public types_TypedElement getTypes_typedelement() {
        return types_typedelement;
    }

    public void setTypes_typedelement(types_TypedElement types_typedelement) {
        this.types_typedelement = types_typedelement;
    }
    public List<types_TypeConstraint> getTypes_typeconstraints() {
        return types_typeconstraints;
    }

    public void addTypes_typeconstraint(Types_typeconstraint types_typeconstraint) {
        this.types_typeconstraints.add(types_typeconstraint);
    }

}