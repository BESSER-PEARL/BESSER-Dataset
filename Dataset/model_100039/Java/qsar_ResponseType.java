





import java.util.List;
import java.util.ArrayList;

public class qsar_ResponseType  {

    private String structureID;
    private String unit;
    private String value;





    private qsar_ResponsesListType qsar_responseslisttype;


    public qsar_ResponseType(
        String structureID,        String unit,        String value    ) {
        this.structureID = structureID;
        this.unit = unit;
        this.value = value;
    }


    public String getStructureid() {
        return structureID;
    }

    public void setStructureid(String structureID) {
        this.structureID = structureID;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public qsar_ResponsesListType getQsar_responseslisttype() {
        return qsar_responseslisttype;
    }

    public void setQsar_responseslisttype(qsar_ResponsesListType qsar_responseslisttype) {
        this.qsar_responseslisttype = qsar_responseslisttype;
    }

}