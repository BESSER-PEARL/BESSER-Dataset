





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_SrcAddressSwitch extends SrcSwitch {

    private String subField;
    private String field;



    public jointPackage_CPL2SPL_SrcAddressSwitch(
        String subField,        String field    ) {
        super(
        );
        this.subField = subField;
        this.field = field;
    }


    public String getSubfield() {
        return subField;
    }

    public void setSubfield(String subField) {
        this.subField = subField;
    }
    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }


}