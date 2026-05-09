





import java.util.List;
import java.util.ArrayList;

public class JTLMM_imperativeocl_AnonymousTupleType extends Class {






    private List<Type> types;


    public JTLMM_imperativeocl_AnonymousTupleType(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public JTLMM_imperativeocl_AnonymousTupleType(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}