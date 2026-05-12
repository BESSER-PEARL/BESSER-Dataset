





import java.util.List;
import java.util.ArrayList;

public class requirement_IdentifiedElement extends EModelElement {

    private String shortDescription;
    private String identifier;



    public requirement_IdentifiedElement(
        String shortDescription,        String identifier    ) {
        super(
        );
        this.shortDescription = shortDescription;
        this.identifier = identifier;
    }


    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}