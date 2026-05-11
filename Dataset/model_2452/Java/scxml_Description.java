





import java.util.List;
import java.util.ArrayList;

public class scxml_Description  {

    private String value;





    private scxml_DescriptionContainer scxml_descriptioncontainer;


    public scxml_Description(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public scxml_DescriptionContainer getScxml_descriptioncontainer() {
        return scxml_descriptioncontainer;
    }

    public void setScxml_descriptioncontainer(scxml_DescriptionContainer scxml_descriptioncontainer) {
        this.scxml_descriptioncontainer = scxml_descriptioncontainer;
    }

}