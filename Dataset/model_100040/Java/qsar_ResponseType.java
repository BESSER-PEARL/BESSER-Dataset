





import java.util.List;
import java.util.ArrayList;

public class qsar_ResponseType  {

    private String arrayValues;
    private String unit;
    private String value;
    private String structureID;





    private qsar_ResponsesListType qsar_responseslisttype;


    public qsar_ResponseType(
        String arrayValues,        String unit,        String value,        String structureID    ) {
        this.arrayValues = arrayValues;
        this.unit = unit;
        this.value = value;
        this.structureID = structureID;
    }


    public String getArrayvalues() {
        return arrayValues;
    }

    public void setArrayvalues(String arrayValues) {
        this.arrayValues = arrayValues;
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
    public String getStructureid() {
        return structureID;
    }

    public void setStructureid(String structureID) {
        this.structureID = structureID;
    }

    public qsar_ResponsesListType getQsar_responseslisttype() {
        return qsar_responseslisttype;
    }

    public void setQsar_responseslisttype(qsar_ResponsesListType qsar_responseslisttype) {
        this.qsar_responseslisttype = qsar_responseslisttype;
    }

}