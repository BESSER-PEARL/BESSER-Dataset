





import java.util.List;
import java.util.ArrayList;

public class aml_Creator  {

    private String objectType;
    private String idRef;
    private String description;





    private aml_MetaData aml_metadata;




    private aml_Memo aml_memo;


    public aml_Creator(
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
    public aml_Memo getAml_memo() {
        return aml_memo;
    }

    public void setAml_memo(aml_Memo aml_memo) {
        this.aml_memo = aml_memo;
    }

}