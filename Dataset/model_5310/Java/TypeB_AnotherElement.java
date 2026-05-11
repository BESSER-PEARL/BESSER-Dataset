





import java.util.List;
import java.util.ArrayList;

public class TypeB_AnotherElement  {

    private String type;
    private String nameElement;
    private String additionalField;
    private String abstractBaseName;



    public TypeB_AnotherElement(
        String type,        String nameElement,        String additionalField,        String abstractBaseName    ) {
        this.type = type;
        this.nameElement = nameElement;
        this.additionalField = additionalField;
        this.abstractBaseName = abstractBaseName;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getNameelement() {
        return nameElement;
    }

    public void setNameelement(String nameElement) {
        this.nameElement = nameElement;
    }
    public String getAdditionalfield() {
        return additionalField;
    }

    public void setAdditionalfield(String additionalField) {
        this.additionalField = additionalField;
    }
    public String getAbstractbasename() {
        return abstractBaseName;
    }

    public void setAbstractbasename(String abstractBaseName) {
        this.abstractBaseName = abstractBaseName;
    }


}