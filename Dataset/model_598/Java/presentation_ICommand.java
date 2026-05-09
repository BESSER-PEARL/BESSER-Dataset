





import java.util.List;
import java.util.ArrayList;

public class presentation_ICommand  {

    private String mixed;





    private presentation_Button presentation_button;


    public presentation_ICommand(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_Button getPresentation_button() {
        return presentation_button;
    }

    public void setPresentation_button(presentation_Button presentation_button) {
        this.presentation_button = presentation_button;
    }

}