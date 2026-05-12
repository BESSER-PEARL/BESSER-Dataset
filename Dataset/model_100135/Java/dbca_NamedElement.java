





import java.util.List;
import java.util.ArrayList;

public class dbca_NamedElement extends CommentedElement {

    private String name;



    public dbca_NamedElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}