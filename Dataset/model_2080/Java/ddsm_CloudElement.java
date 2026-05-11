





import java.util.List;
import java.util.ArrayList;

public class ddsm_CloudElement  {

    private String description;
    private String elementId;



    public ddsm_CloudElement(
        String description,        String elementId    ) {
        this.description = description;
        this.elementId = elementId;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getElementid() {
        return elementId;
    }

    public void setElementid(String elementId) {
        this.elementId = elementId;
    }


}