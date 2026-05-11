





import java.util.List;
import java.util.ArrayList;

public class aml_Creator  {

    private String idRef;
    private String description;
    private String objectType;





    private aml_Memo aml_memo;




    private aml_MetaData aml_metadata;


    public aml_Creator(
        String idRef,        String description,        String objectType    ) {
        this.idRef = idRef;
        this.description = description;
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
    public String getObjecttype() {
        return objectType;
    }

    public void setObjecttype(String objectType) {
        this.objectType = objectType;
    }

    public aml_Memo getAml_memo() {
        return aml_memo;
    }

    public void setAml_memo(aml_Memo aml_memo) {
        this.aml_memo = aml_memo;
    }
    public aml_MetaData getAml_metadata() {
        return aml_metadata;
    }

    public void setAml_metadata(aml_MetaData aml_metadata) {
        this.aml_metadata = aml_metadata;
    }

}