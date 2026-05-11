





import java.util.List;
import java.util.ArrayList;

public class types_Type extends PackageMember {






    private types_ArrayType types_arraytype;




    private List<types_TypeConstraint> types_typeconstraints;




    private types_TypeParameter types_typeparameter;


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


    public types_ArrayType getTypes_arraytype() {
        return types_arraytype;
    }

    public void setTypes_arraytype(types_ArrayType types_arraytype) {
        this.types_arraytype = types_arraytype;
    }
    public List<types_TypeConstraint> getTypes_typeconstraints() {
        return types_typeconstraints;
    }

    public void addTypes_typeconstraint(Types_typeconstraint types_typeconstraint) {
        this.types_typeconstraints.add(types_typeconstraint);
    }
    public types_TypeParameter getTypes_typeparameter() {
        return types_typeparameter;
    }

    public void setTypes_typeparameter(types_TypeParameter types_typeparameter) {
        this.types_typeparameter = types_typeparameter;
    }

}