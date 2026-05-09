





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaDataField extends JavaElement {

    private String FieldValue;





    private PSM_JavaDataType psm_javadatatype;


    public PSM_JavaDataField(
        String FieldValue    ) {
        super(
        );
        this.FieldValue = FieldValue;
    }


    public String getFieldvalue() {
        return FieldValue;
    }

    public void setFieldvalue(String FieldValue) {
        this.FieldValue = FieldValue;
    }

    public PSM_JavaDataType getPsm_javadatatype() {
        return psm_javadatatype;
    }

    public void setPsm_javadatatype(PSM_JavaDataType psm_javadatatype) {
        this.psm_javadatatype = psm_javadatatype;
    }

}