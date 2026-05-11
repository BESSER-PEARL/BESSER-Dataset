





import java.util.List;
import java.util.ArrayList;

public class aml_Publisher  {

    private String objectType;
    private String idRef;
    private String description;





    private aml_MetaData aml_metadata;




    private aml_DocumentRoot aml_documentroot;


    public aml_Publisher(
        String objectType,        String idRef,        String description    ) {
        this.objectType = objectType;
        this.idRef = idRef;
        this.description = description;
    }


    public String getObjecttype() {
        return objectType;
    }

    public void setObjecttype(String objectType) {
        this.objectType = objectType;
    }
    public String getIdref() {
        return idRef;
    }

    public void setIdref(String idRef) {
        this.idRef = idRef;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public aml_MetaData getAml_metadata() {
        return aml_metadata;
    }

    public void setAml_metadata(aml_MetaData aml_metadata) {
        this.aml_metadata = aml_metadata;
    }
    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }

}