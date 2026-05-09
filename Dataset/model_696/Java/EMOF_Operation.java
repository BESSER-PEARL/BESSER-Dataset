





import java.util.List;
import java.util.ArrayList;

public class EMOF_Operation extends TypedElement, MultiplicityElement {






    private Class class;




    private List<Type> types;


    public EMOF_Operation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public EMOF_Operation(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}