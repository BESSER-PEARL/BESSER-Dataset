





import java.util.List;
import java.util.ArrayList;

public class presentation_Shell extends Decorations {

    private String minimumSize;
    private String imeInputMode;
    private String fullScreen;
    private String alpha;
    private String group5;





    private presentation_ToolTip presentation_tooltip;




    private List<presentation_Shell> presentation_shells;


    public presentation_Shell(
        String minimumSize,        String imeInputMode,        String fullScreen,        String alpha,        String group5    ) {
        super(
        );
        this.minimumSize = minimumSize;
        this.imeInputMode = imeInputMode;
        this.fullScreen = fullScreen;
        this.alpha = alpha;
        this.group5 = group5;
        this.presentation_shells = new ArrayList<>();
    }

    public presentation_Shell(
        String minimumSize,        String imeInputMode,        String fullScreen,        String alpha,        String group5        ArrayList<presentation_Shell> presentation_shells    ) {
        this.minimumSize = minimumSize;
        this.imeInputMode = imeInputMode;
        this.fullScreen = fullScreen;
        this.alpha = alpha;
        this.group5 = group5;
        this.presentation_shells = presentation_shells;
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
    public String getFullscreen() {
        return fullScreen;
    }

    public void setFullscreen(String fullScreen) {
        this.fullScreen = fullScreen;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getGroup5() {
        return group5;
    }

    public void setGroup5(String group5) {
        this.group5 = group5;
    }

    public presentation_ToolTip getPresentation_tooltip() {
        return presentation_tooltip;
    }

    public void setPresentation_tooltip(presentation_ToolTip presentation_tooltip) {
        this.presentation_tooltip = presentation_tooltip;
    }
    public List<presentation_Shell> getPresentation_shells() {
        return presentation_shells;
    }

    public void addPresentation_shell(Presentation_shell presentation_shell) {
        this.presentation_shells.add(presentation_shell);
    }

}