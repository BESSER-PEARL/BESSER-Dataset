





import java.util.List;
import java.util.ArrayList;

public class JTL_emof_Operation extends emof_MultiplicityElement, emof_TypedElement {






    private List<Type> types;




    private Class class;


    public JTL_emof_Operation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public JTL_emof_Operation(
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