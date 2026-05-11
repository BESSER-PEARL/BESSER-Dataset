





import java.util.List;
import java.util.ArrayList;

public class architecture_extension_Role extends AnalysedElement {

    private String attachedElement;



    public architecture_extension_Role(
        String attachedElement    ) {
        super(
        );
        this.attachedElement = attachedElement;
    }


    public String getAttachedelement() {
        return attachedElement;
    }

    public void setAttachedelement(String attachedElement) {
        this.attachedElement = attachedElement;
    }


}