





import java.util.List;
import java.util.ArrayList;

public class c_sharp_types_PointerType extends types_Type, types_NonArrayType {






    private ReferenceType referencetype;




    private SimpleType simpletype;


    public c_sharp_types_PointerType(
    ) {
        super(
        );
    }



    public ReferenceType getReferencetype() {
        return referencetype;
    }

    public void setReferencetype(ReferenceType referencetype) {
        this.referencetype = referencetype;
    }
    public SimpleType getSimpletype() {
        return simpletype;
    }

    public void setSimpletype(SimpleType simpletype) {
        this.simpletype = simpletype;
    }

}