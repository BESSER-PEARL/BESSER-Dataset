





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDNotationDeclaration extends xsd_XSDNamedComponent, xsd_XSDSchemaContent {

    private String systemIdentifier;
    private String publicIdentifier;



    public model_xsd_XSDNotationDeclaration(
        String systemIdentifier,        String publicIdentifier    ) {
        super(
        );
        this.systemIdentifier = systemIdentifier;
        this.publicIdentifier = publicIdentifier;
    }


    public String getSystemidentifier() {
        return systemIdentifier;
    }

    public void setSystemidentifier(String systemIdentifier) {
        this.systemIdentifier = systemIdentifier;
    }
    public String getPublicidentifier() {
        return publicIdentifier;
    }

    public void setPublicidentifier(String publicIdentifier) {
        this.publicIdentifier = publicIdentifier;
    }


}