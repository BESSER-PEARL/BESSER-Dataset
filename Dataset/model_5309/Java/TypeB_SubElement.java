





import java.util.List;
import java.util.ArrayList;

public class TypeB_SubElement extends Element {

    private String additionalField;



    public TypeB_SubElement(
        String additionalField    ) {
        super(
        );
        this.additionalField = additionalField;
    }


    public String getAdditionalfield() {
        return additionalField;
    }

    public void setAdditionalfield(String additionalField) {
        this.additionalField = additionalField;
    }


}