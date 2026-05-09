





import java.util.List;
import java.util.ArrayList;

public class DOM_ClassInstanceCreation extends Expression {






    private List<Type> types;




    private Type type;


    public DOM_ClassInstanceCreation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public DOM_ClassInstanceCreation(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}