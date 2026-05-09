





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaElement extends ArtifactElement {

    private String ElementIdentifier;
    private String ElementProfile;



    public PSM_JavaElement(
        String ElementIdentifier,        String ElementProfile    ) {
        super(
        );
        this.ElementIdentifier = ElementIdentifier;
        this.ElementProfile = ElementProfile;
    }


    public String getElementidentifier() {
        return ElementIdentifier;
    }

    public void setElementidentifier(String ElementIdentifier) {
        this.ElementIdentifier = ElementIdentifier;
    }
    public String getElementprofile() {
        return ElementProfile;
    }

    public void setElementprofile(String ElementProfile) {
        this.ElementProfile = ElementProfile;
    }


}