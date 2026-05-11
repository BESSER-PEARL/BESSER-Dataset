





import java.util.List;
import java.util.ArrayList;

public class model_Window extends SkinSupport, Widget, ColorBackgroundSupport, VerticalScrollbarSupport, ColorAlphaSupport {

    private boolean minimizeButton;
    private boolean maximizeButton;
    private boolean closeButton;



    public model_Window(
        boolean minimizeButton,        boolean maximizeButton,        boolean closeButton    ) {
        super(
        );
        this.minimizeButton = minimizeButton;
        this.maximizeButton = maximizeButton;
        this.closeButton = closeButton;
    }


    public boolean getMinimizebutton() {
        return minimizeButton;
    }

    public void setMinimizebutton(boolean minimizeButton) {
        this.minimizeButton = minimizeButton;
    }
    public boolean getMaximizebutton() {
        return maximizeButton;
    }

    public void setMaximizebutton(boolean maximizeButton) {
        this.maximizeButton = maximizeButton;
    }
    public boolean getClosebutton() {
        return closeButton;
    }

    public void setClosebutton(boolean closeButton) {
        this.closeButton = closeButton;
    }


}