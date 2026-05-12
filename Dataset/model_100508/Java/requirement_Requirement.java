





import java.util.List;
import java.util.ArrayList;

public class requirement_Requirement extends IdentifiedElement {

    private String externalResources;



    public requirement_Requirement(
        String externalResources    ) {
        super(
        );
        this.externalResources = externalResources;
    }


    public String getExternalresources() {
        return externalResources;
    }

    public void setExternalresources(String externalResources) {
        this.externalResources = externalResources;
    }


}