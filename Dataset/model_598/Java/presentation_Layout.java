





import java.util.List;
import java.util.ArrayList;

public class presentation_Layout  {

    private String mixed;





    private presentation_Composite presentation_composite;


    public presentation_Layout(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_Composite getPresentation_composite() {
        return presentation_composite;
    }

    public void setPresentation_composite(presentation_Composite presentation_composite) {
        this.presentation_composite = presentation_composite;
    }

}