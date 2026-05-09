





import java.util.List;
import java.util.ArrayList;

public class presentation_IDialogBlockedHandler  {

    private String mixed;





    private presentation_Dialog presentation_dialog;


    public presentation_IDialogBlockedHandler(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_Dialog getPresentation_dialog() {
        return presentation_dialog;
    }

    public void setPresentation_dialog(presentation_Dialog presentation_dialog) {
        this.presentation_dialog = presentation_dialog;
    }

}