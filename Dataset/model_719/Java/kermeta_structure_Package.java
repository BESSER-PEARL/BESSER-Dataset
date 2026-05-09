





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Package extends structure_NamedElement, structure_TypeDefinitionContainer {

    private String uri;



    public kermeta_structure_Package(
        String uri    ) {
        super(
        );
        this.uri = uri;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}