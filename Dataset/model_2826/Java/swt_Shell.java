





import java.util.List;
import java.util.ArrayList;

public class swt_Shell extends Decorations {

    private String modalStyle;
    private String trimStyle;
    private boolean fullScreen;
    private int alpha;





    private swt_Button swt_button;


    public swt_Shell(
        String modalStyle,        String trimStyle,        boolean fullScreen,        int alpha    ) {
        super(
        );
        this.modalStyle = modalStyle;
        this.trimStyle = trimStyle;
        this.fullScreen = fullScreen;
        this.alpha = alpha;
    }


    public String getModalstyle() {
        return modalStyle;
    }

    public void setModalstyle(String modalStyle) {
        this.modalStyle = modalStyle;
    }
    public String getTrimstyle() {
        return trimStyle;
    }

    public void setTrimstyle(String trimStyle) {
        this.trimStyle = trimStyle;
    }
    public boolean getFullscreen() {
        return fullScreen;
    }

    public void setFullscreen(boolean fullScreen) {
        this.fullScreen = fullScreen;
    }
    public int getAlpha() {
        return alpha;
    }

    public void setAlpha(int alpha) {
        this.alpha = alpha;
    }

    public swt_Button getSwt_button() {
        return swt_button;
    }

    public void setSwt_button(swt_Button swt_button) {
        this.swt_button = swt_button;
    }

}