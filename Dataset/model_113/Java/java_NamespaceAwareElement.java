





import java.util.List;
import java.util.ArrayList;

public class java_NamespaceAwareElement extends Commentable {

    private String namespaces;



    public java_NamespaceAwareElement(
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