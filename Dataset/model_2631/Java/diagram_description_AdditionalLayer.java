





import java.util.List;
import java.util.ArrayList;

public class diagram_description_AdditionalLayer extends Layer {

    private boolean optional;
    private boolean activeByDefault;



    public diagram_description_AdditionalLayer(
        boolean optional,        boolean activeByDefault    ) {
        super(
        );
        this.optional = optional;
        this.activeByDefault = activeByDefault;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public boolean getActivebydefault() {
        return activeByDefault;
    }

    public void setActivebydefault(boolean activeByDefault) {
        this.activeByDefault = activeByDefault;
    }


}