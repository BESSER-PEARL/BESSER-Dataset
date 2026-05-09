





import java.util.List;
import java.util.ArrayList;

public class DOM_SuperMethodInvocation extends Expression {






    private List<Type> types;




    private Name name;




    private Name name;


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


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
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

}