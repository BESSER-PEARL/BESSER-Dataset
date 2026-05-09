





import java.util.List;
import java.util.ArrayList;

public class DOM_SuperMethodInvocation extends Expression {






    private Name name;




    private Name name;




    private List<Type> types;


    public DOM_SuperMethodInvocation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public DOM_SuperMethodInvocation(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public Name getName() {
        return name;
    }

    public void setName(Name name) {
        this.name = name;
    }
    public Name getName() {
        return name;
    }

    public void setName(Name name) {
        this.name = name;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}