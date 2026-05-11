





import java.util.List;
import java.util.ArrayList;

public class form_SelectionField extends InputField {

    private String selectionFieldType;



    public form_SelectionField(
        String selectionFieldType    ) {
        super(
        );
        this.selectionFieldType = selectionFieldType;
    }


    public String getSelectionfieldtype() {
        return selectionFieldType;
    }

    public void setSelectionfieldtype(String selectionFieldType) {
        this.selectionFieldType = selectionFieldType;
    }


}