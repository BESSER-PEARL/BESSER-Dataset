





import java.util.List;
import java.util.ArrayList;

public class presentation_Shell extends Decorations {

    private String minimumSize;
    private String imeInputMode;
    private String group5;
    private String alpha;
    private String fullScreen;





    private presentation_Shell presentation_shell;




    private presentation_ToolTip presentation_tooltip;


    public presentation_Shell(
        String minimumSize,        String imeInputMode,        String group5,        String alpha,        String fullScreen    ) {
        super(
        );
        this.minimumSize = minimumSize;
        this.imeInputMode = imeInputMode;
        this.group5 = group5;
        this.alpha = alpha;
        this.fullScreen = fullScreen;
    }


    public String getMinimumsize() {
        return minimumSize;
    }

    public void setMinimumsize(String minimumSize) {
        this.minimumSize = minimumSize;
    }
    public String getImeinputmode() {
        return imeInputMode;
    }

    public void setImeinputmode(String imeInputMode) {
        this.imeInputMode = imeInputMode;
    }
    public String getGroup5() {
        return group5;
    }

    public void setGroup5(String group5) {
        this.group5 = group5;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getFullscreen() {
        return fullScreen;
    }

    public void setFullscreen(String fullScreen) {
        this.fullScreen = fullScreen;
    }

    public presentation_Shell getPresentation_shell() {
        return presentation_shell;
    }

    public void setPresentation_shell(presentation_Shell presentation_shell) {
        this.presentation_shell = presentation_shell;
    }
    public presentation_ToolTip getPresentation_tooltip() {
        return presentation_tooltip;
    }

    public void setPresentation_tooltip(presentation_ToolTip presentation_tooltip) {
        this.presentation_tooltip = presentation_tooltip;
    }

}