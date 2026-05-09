





import java.util.List;
import java.util.ArrayList;

public class presentation_WindowManager  {

    private String mixed;





    private presentation_Window presentation_window;


    public presentation_WindowManager(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_Window getPresentation_window() {
        return presentation_window;
    }

    public void setPresentation_window(presentation_Window presentation_window) {
        this.presentation_window = presentation_window;
    }

}