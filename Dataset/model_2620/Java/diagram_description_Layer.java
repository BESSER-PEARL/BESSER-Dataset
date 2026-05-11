





import java.util.List;
import java.util.ArrayList;

public class diagram_description_Layer extends description_DocumentedElement, description_IdentifiedElement, description_EndUserDocumentedElement {

    private String icon;



    public diagram_description_Layer(
        String icon    ) {
        super(
        );
        this.icon = icon;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }


}