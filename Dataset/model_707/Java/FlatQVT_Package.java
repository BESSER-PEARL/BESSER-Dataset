





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_Package extends NamedElement {

    private String uri;





    private List<Type> types;


    public FlatQVT_Package(
        String uri    ) {
        super(
        );
        this.uri = uri;
        this.types = new ArrayList<>();
    }

    public FlatQVT_Package(
        String uri        ArrayList<Type> types    ) {
        this.uri = uri;
        this.types = types;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}