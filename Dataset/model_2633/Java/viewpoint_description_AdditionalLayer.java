





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_AdditionalLayer extends Layer {

    private boolean activeByDefault;
    private boolean optional;



    public viewpoint_description_AdditionalLayer(
        boolean activeByDefault,        boolean optional    ) {
        super(
        );
        this.activeByDefault = activeByDefault;
        this.optional = optional;
    }


    public boolean getActivebydefault() {
        return activeByDefault;
    }

    public void setActivebydefault(boolean activeByDefault) {
        this.activeByDefault = activeByDefault;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }


}