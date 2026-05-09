





import java.util.List;
import java.util.ArrayList;

public class emof_Operation extends TypedElement, MultiplicityElement {






    private List<Type> types;




    private Class class;


    public emof_Operation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public emof_Operation(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }

}