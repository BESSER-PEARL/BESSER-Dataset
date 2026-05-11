





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Import extends wsdl_IImport, wsdl_ExtensibleElement {

    private String locationURI;
    private String namespaceURI;



    public model_wsdl_Import(
        String locationURI,        String namespaceURI    ) {
        super(
        );
        this.locationURI = locationURI;
        this.namespaceURI = namespaceURI;
    }


    public String getLocationuri() {
        return locationURI;
    }

    public void setLocationuri(String locationURI) {
        this.locationURI = locationURI;
    }
    public String getNamespaceuri() {
        return namespaceURI;
    }

    public void setNamespaceuri(String namespaceURI) {
        this.namespaceURI = namespaceURI;
    }


}