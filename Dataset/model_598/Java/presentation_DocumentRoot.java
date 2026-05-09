





import java.util.List;
import java.util.ArrayList;

public class presentation_DocumentRoot  {

    private String mixed;





    private List<presentation_Composite> presentation_composites;


    public presentation_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.presentation_composites = new ArrayList<>();
    }

    public presentation_DocumentRoot(
        String mixed        ArrayList<presentation_Composite> presentation_composites    ) {
        this.mixed = mixed;
        this.presentation_composites = presentation_composites;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<presentation_Composite> getPresentation_composites() {
        return presentation_composites;
    }

    public void addPresentation_composite(Presentation_composite presentation_composite) {
        this.presentation_composites.add(presentation_composite);
    }

}