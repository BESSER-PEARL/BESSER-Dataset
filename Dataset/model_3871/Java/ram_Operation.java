





import java.util.List;
import java.util.ArrayList;

public class ram_Operation extends NamedElement, MappableElement {

    private String visibility;
    private boolean partial;
    private boolean abstract;
    private boolean static;





    private ram_AspectMessageView ram_aspectmessageview;


    public ram_Operation(
        String visibility,        boolean partial,        boolean abstract,        boolean static    ) {
        super(
        );
        this.visibility = visibility;
        this.partial = partial;
        this.abstract = abstract;
        this.static = static;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getPartial() {
        return partial;
    }

    public void setPartial(boolean partial) {
        this.partial = partial;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public ram_AspectMessageView getRam_aspectmessageview() {
        return ram_aspectmessageview;
    }

    public void setRam_aspectmessageview(ram_AspectMessageView ram_aspectmessageview) {
        this.ram_aspectmessageview = ram_aspectmessageview;
    }

}