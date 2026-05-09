





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_MetamodelDeclaration extends OclMetamodel {

    private String resource;
    private String metamodelURI;



    public gbind_dsl_MetamodelDeclaration(
        String resource,        String metamodelURI    ) {
        super(
        );
        this.resource = resource;
        this.metamodelURI = metamodelURI;
    }


    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }
    public String getMetamodeluri() {
        return metamodelURI;
    }

    public void setMetamodeluri(String metamodelURI) {
        this.metamodelURI = metamodelURI;
    }


}