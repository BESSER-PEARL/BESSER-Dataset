





import java.util.List;
import java.util.ArrayList;

public class pcm_av_seff_av_EmitEventAction extends seff_av_CallAction, seff_av_AbstractAction {






    private EventType eventtype;




    private SourceRole sourcerole;


    public pcm_av_seff_av_EmitEventAction(
    ) {
        super(
        );
    }



    public EventType getEventtype() {
        return eventtype;
    }

    public void setEventtype(EventType eventtype) {
        this.eventtype = eventtype;
    }
    public SourceRole getSourcerole() {
        return sourcerole;
    }

    public void setSourcerole(SourceRole sourcerole) {
        this.sourcerole = sourcerole;
    }

}