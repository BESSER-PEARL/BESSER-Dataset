





import java.util.List;
import java.util.ArrayList;

public class aml_CollectionItem  {

    private String ordinal;
    private String objectType;
    private String idRef;





    private aml_Collection aml_collection;


    public aml_CollectionItem(
        String ordinal,        String objectType,        String idRef    ) {
        this.ordinal = ordinal;
        this.objectType = objectType;
        this.idRef = idRef;
    }


    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
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

    public aml_Collection getAml_collection() {
        return aml_collection;
    }

    public void setAml_collection(aml_Collection aml_collection) {
        this.aml_collection = aml_collection;
    }

}