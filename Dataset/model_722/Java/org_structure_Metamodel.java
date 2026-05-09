





import java.util.List;
import java.util.ArrayList;

public class org_structure_Metamodel extends structure_KermetaModelElement, structure_NamedElement, structure_ModelTypeDefinitionContainer {

    private boolean isResolved;
    private String uri;



    public org_structure_Metamodel(
        boolean isResolved,        String uri    ) {
        super(
        );
        this.isResolved = isResolved;
        this.uri = uri;
    }


    public boolean getIsresolved() {
        return isResolved;
    }

    public void setIsresolved(boolean isResolved) {
        this.isResolved = isResolved;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}