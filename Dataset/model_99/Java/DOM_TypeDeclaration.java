





import java.util.List;
import java.util.ArrayList;

public class DOM_TypeDeclaration extends AbstractTypeDeclaration {

    private String interface;





    private Type type;




    private List<Type> types;


    public DOM_TypeDeclaration(
        String interface    ) {
        super(
        );
        this.interface = interface;
        this.types = new ArrayList<>();
    }

    public DOM_TypeDeclaration(
        String interface        ArrayList<Type> types    ) {
        this.interface = interface;
        this.types = types;
    }

    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}