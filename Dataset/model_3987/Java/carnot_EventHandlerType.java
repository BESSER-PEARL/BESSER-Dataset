





import java.util.List;
import java.util.ArrayList;

public class carnot_EventHandlerType extends IIdentifiableModelElement, ITypedElement, IAccessPointOwner {

    private String unbindOnMatch;
    private String consumeOnMatch;
    private String autoBind;
    private String logHandler;





    private carnot_IEventHandlerOwner carnot_ieventhandlerowner;


    public carnot_EventHandlerType(
        String unbindOnMatch,        String consumeOnMatch,        String autoBind,        String logHandler    ) {
        super(
        );
        this.unbindOnMatch = unbindOnMatch;
        this.consumeOnMatch = consumeOnMatch;
        this.autoBind = autoBind;
        this.logHandler = logHandler;
    }


    public String getUnbindonmatch() {
        return unbindOnMatch;
    }

    public void setUnbindonmatch(String unbindOnMatch) {
        this.unbindOnMatch = unbindOnMatch;
    }
    public String getConsumeonmatch() {
        return consumeOnMatch;
    }

    public void setConsumeonmatch(String consumeOnMatch) {
        this.consumeOnMatch = consumeOnMatch;
    }
    public String getAutobind() {
        return autoBind;
    }

    public void setAutobind(String autoBind) {
        this.autoBind = autoBind;
    }
    public String getLoghandler() {
        return logHandler;
    }

    public void setLoghandler(String logHandler) {
        this.logHandler = logHandler;
    }

    public carnot_IEventHandlerOwner getCarnot_ieventhandlerowner() {
        return carnot_ieventhandlerowner;
    }

    public void setCarnot_ieventhandlerowner(carnot_IEventHandlerOwner carnot_ieventhandlerowner) {
        this.carnot_ieventhandlerowner = carnot_ieventhandlerowner;
    }

}