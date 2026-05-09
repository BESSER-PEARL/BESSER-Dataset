





import java.util.List;
import java.util.ArrayList;

public class org_structure_Metamodel extends structure_KermetaModelElement, structure_NamedElement, structure_ModelTypeDefinitionContainer {

    private String uri;
    private boolean isResolved;



    public org_structure_Metamodel(
        String uri,        boolean isResolved    ) {
        super(
        );
        this.uri = uri;
        this.isResolved = isResolved;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public boolean getIsresolved() {
        return isResolved;
    }

    public void setIsresolved(boolean isResolved) {
        this.isResolved = isResolved;
    }


}