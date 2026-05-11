





import java.util.List;
import java.util.ArrayList;

public class model_Window extends ColorAlphaSupport, Widget, VerticalScrollbarSupport, SkinSupport, ColorBackgroundSupport {

    private boolean closeButton;
    private boolean maximizeButton;
    private boolean minimizeButton;



    public model_Window(
        boolean closeButton,        boolean maximizeButton,        boolean minimizeButton    ) {
        super(
        );
        this.closeButton = closeButton;
        this.maximizeButton = maximizeButton;
        this.minimizeButton = minimizeButton;
    }


    public boolean getClosebutton() {
        return closeButton;
    }

    public void setClosebutton(boolean closeButton) {
        this.closeButton = closeButton;
    }
    public boolean getMaximizebutton() {
        return maximizeButton;
    }

    public void setMaximizebutton(boolean maximizeButton) {
        this.maximizeButton = maximizeButton;
    }
    public boolean getMinimizebutton() {
        return minimizeButton;
    }

    public void setMinimizebutton(boolean minimizeButton) {
        this.minimizeButton = minimizeButton;
    }


}