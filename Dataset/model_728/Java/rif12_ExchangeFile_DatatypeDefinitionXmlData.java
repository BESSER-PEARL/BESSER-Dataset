





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_DatatypeDefinitionXmlData extends DatatypeDefinitionComplex {

    private String nameSpaceURI;
    private String schemaLocation;



    public rif12_ExchangeFile_DatatypeDefinitionXmlData(
        String nameSpaceURI,        String schemaLocation    ) {
        super(
        );
        this.nameSpaceURI = nameSpaceURI;
        this.schemaLocation = schemaLocation;
    }


    public String getNamespaceuri() {
        return nameSpaceURI;
    }

    public void setNamespaceuri(String nameSpaceURI) {
        this.nameSpaceURI = nameSpaceURI;
    }
    public String getSchemalocation() {
        return schemaLocation;
    }

    public void setSchemalocation(String schemaLocation) {
        this.schemaLocation = schemaLocation;
    }


}