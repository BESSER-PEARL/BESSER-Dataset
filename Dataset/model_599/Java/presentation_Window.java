





import java.util.List;
import java.util.ArrayList;

public class presentation_Window  {

    private String group;
    private String blockOnOpen;
    private String mixed;





    private List<presentation_WindowManager> presentation_windowmanagers;




    private presentation_DocumentRoot presentation_documentroot;


    public presentation_Window(
        String group,        String blockOnOpen,        String mixed    ) {
        this.group = group;
        this.blockOnOpen = blockOnOpen;
        this.mixed = mixed;
        this.presentation_windowmanagers = new ArrayList<>();
    }

    public presentation_Window(
        String group,        String blockOnOpen,        String mixed        ArrayList<presentation_WindowManager> presentation_windowmanagers    ) {
        this.group = group;
        this.blockOnOpen = blockOnOpen;
        this.mixed = mixed;
        this.presentation_windowmanagers = presentation_windowmanagers;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getBlockonopen() {
        return blockOnOpen;
    }

    public void setBlockonopen(String blockOnOpen) {
        this.blockOnOpen = blockOnOpen;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<presentation_WindowManager> getPresentation_windowmanagers() {
        return presentation_windowmanagers;
    }

    public void addPresentation_windowmanager(Presentation_windowmanager presentation_windowmanager) {
        this.presentation_windowmanagers.add(presentation_windowmanager);
    }
    public presentation_DocumentRoot getPresentation_documentroot() {
        return presentation_documentroot;
    }

    public void setPresentation_documentroot(presentation_DocumentRoot presentation_documentroot) {
        this.presentation_documentroot = presentation_documentroot;
    }

}