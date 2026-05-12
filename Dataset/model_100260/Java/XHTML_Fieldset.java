





import java.util.List;
import java.util.ArrayList;

public class XHTML_Fieldset extends Attrs, block {






    private List<FieldsetElement> fieldsetelements;


    public XHTML_Fieldset(
    ) {
        super(
        );
        this.fieldsetelements = new ArrayList<>();
    }

    public XHTML_Fieldset(
        ArrayList<FieldsetElement> fieldsetelements    ) {
        this.fieldsetelements = fieldsetelements;
    }


    public List<FieldsetElement> getFieldsetelements() {
        return fieldsetelements;
    }

    public void addFieldsetelement(Fieldsetelement fieldsetelement) {
        this.fieldsetelements.add(fieldsetelement);
    }

}