





import java.util.List;
import java.util.ArrayList;

public class model_OnEvent extends BPELExtensibleElement {






    private model_EventHandler model_eventhandler;




    private model_FromParts model_fromparts;


    public model_OnEvent(
    ) {
        super(
        );
    }



    public model_EventHandler getModel_eventhandler() {
        return model_eventhandler;
    }

    public void setModel_eventhandler(model_EventHandler model_eventhandler) {
        this.model_eventhandler = model_eventhandler;
    }
    public model_FromParts getModel_fromparts() {
        return model_fromparts;
    }

    public void setModel_fromparts(model_FromParts model_fromparts) {
        this.model_fromparts = model_fromparts;
    }

}