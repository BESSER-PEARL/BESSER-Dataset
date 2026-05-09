





import java.util.List;
import java.util.ArrayList;

public class commons_NamespaceAwareElement extends Commentable {

    private String namespaces;



    public commons_NamespaceAwareElement(
        String namespaces    ) {
        super(
        );
        this.namespaces = namespaces;
    }


    public String getNamespaces() {
        return namespaces;
    }

    public void setNamespaces(String namespaces) {
        this.namespaces = namespaces;
    }


}