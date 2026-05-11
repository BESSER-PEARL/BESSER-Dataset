





import java.util.List;
import java.util.ArrayList;

public class ram_Operation extends NamedElement, MappableElement {

    private boolean abstract;
    private String visibility;
    private boolean static;
    private boolean partial;





    private ram_Transition ram_transition;




    private ram_AspectMessageView ram_aspectmessageview;




    private ram_Type ram_type;


    public ram_Operation(
        boolean abstract,        String visibility,        boolean static,        boolean partial    ) {
        super(
        );
        this.abstract = abstract;
        this.visibility = visibility;
        this.static = static;
        this.partial = partial;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getPartial() {
        return partial;
    }

    public void setPartial(boolean partial) {
        this.partial = partial;
    }

    public ram_Transition getRam_transition() {
        return ram_transition;
    }

    public void setRam_transition(ram_Transition ram_transition) {
        this.ram_transition = ram_transition;
    }
    public ram_AspectMessageView getRam_aspectmessageview() {
        return ram_aspectmessageview;
    }

    public void setRam_aspectmessageview(ram_AspectMessageView ram_aspectmessageview) {
        this.ram_aspectmessageview = ram_aspectmessageview;
    }
    public ram_Type getRam_type() {
        return ram_type;
    }

    public void setRam_type(ram_Type ram_type) {
        this.ram_type = ram_type;
    }

}