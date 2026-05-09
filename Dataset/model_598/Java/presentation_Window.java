





import java.util.List;
import java.util.ArrayList;

public class presentation_Window  {

    private String group;
    private String blockOnOpen;
    private String mixed;





    private presentation_DocumentRoot presentation_documentroot;


    public presentation_Window(
        String group,        String blockOnOpen,        String mixed    ) {
        this.group = group;
        this.blockOnOpen = blockOnOpen;
        this.mixed = mixed;
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

    public presentation_DocumentRoot getPresentation_documentroot() {
        return presentation_documentroot;
    }

    public void setPresentation_documentroot(presentation_DocumentRoot presentation_documentroot) {
        this.presentation_documentroot = presentation_documentroot;
    }

}