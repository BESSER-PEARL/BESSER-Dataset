





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_DatatypeDefinitionXmlData extends DatatypeDefinitionComplex {

    private String schemaLocation;
    private String nameSpaceURI;



    public rif12_ExchangeFile_DatatypeDefinitionXmlData(
        String schemaLocation,        String nameSpaceURI    ) {
        super(
        );
        this.schemaLocation = schemaLocation;
        this.nameSpaceURI = nameSpaceURI;
    }


    public String getSchemalocation() {
        return schemaLocation;
    }

    public void setSchemalocation(String schemaLocation) {
        this.schemaLocation = schemaLocation;
    }
    public String getNamespaceuri() {
        return nameSpaceURI;
    }

    public void setNamespaceuri(String nameSpaceURI) {
        this.nameSpaceURI = nameSpaceURI;
    }


}