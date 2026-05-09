





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_OrderedTupleType extends Class {






    private List<Type> types;


    public ImperativeOCL_OrderedTupleType(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public ImperativeOCL_OrderedTupleType(
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