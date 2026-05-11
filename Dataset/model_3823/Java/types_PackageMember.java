





import java.util.List;
import java.util.ArrayList;

public class types_PackageMember extends NamedElement, AnnotatableElement {

    private String id;



    public types_PackageMember(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}