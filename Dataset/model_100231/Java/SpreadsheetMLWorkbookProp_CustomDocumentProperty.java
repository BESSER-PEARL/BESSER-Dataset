





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_CustomDocumentProperty  {

    private String name;





    private ValueType valuetype;


    public SpreadsheetMLWorkbookProp_CustomDocumentProperty(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ValueType getValuetype() {
        return valuetype;
    }

    public void setValuetype(ValueType valuetype) {
        this.valuetype = valuetype;
    }

}