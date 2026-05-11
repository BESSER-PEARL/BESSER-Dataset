





import java.util.List;
import java.util.ArrayList;

public class aml_CollectionItem  {

    private String ordinal;
    private String idRef;
    private String objectType;





    private aml_Collection aml_collection;


    public aml_CollectionItem(
        String ordinal,        String idRef,        String objectType    ) {
        this.ordinal = ordinal;
        this.idRef = idRef;
        this.objectType = objectType;
    }


    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
    }
    public String getIdref() {
        return idRef;
    }

    public void setIdref(String idRef) {
        this.idRef = idRef;
    }
    public String getObjecttype() {
        return objectType;
    }

    public void setObjecttype(String objectType) {
        this.objectType = objectType;
    }

    public aml_Collection getAml_collection() {
        return aml_collection;
    }

    public void setAml_collection(aml_Collection aml_collection) {
        this.aml_collection = aml_collection;
    }

}