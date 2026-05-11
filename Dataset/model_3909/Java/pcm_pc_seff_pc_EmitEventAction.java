





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_seff_pc_EmitEventAction extends seff_pc_AbstractAction, seff_pc_CallAction {






    private SourceRole sourcerole;




    private EventType eventtype;


    public pcm_pc_seff_pc_EmitEventAction(
    ) {
        super(
        );
    }



    public SourceRole getSourcerole() {
        return sourcerole;
    }

    public void setSourcerole(SourceRole sourcerole) {
        this.sourcerole = sourcerole;
    }
    public EventType getEventtype() {
        return eventtype;
    }

    public void setEventtype(EventType eventtype) {
        this.eventtype = eventtype;
    }

}