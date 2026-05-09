





import java.util.List;
import java.util.ArrayList;

public class Janus_emof_Operation extends emof_TypedElement, emof_MultiplicityElement {






    private Class class;




    private List<Type> types;


    public Janus_emof_Operation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public Janus_emof_Operation(
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