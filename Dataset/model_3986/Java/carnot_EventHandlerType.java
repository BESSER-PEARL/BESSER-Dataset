





import java.util.List;
import java.util.ArrayList;

public class carnot_EventHandlerType extends ITypedElement, IIdentifiableModelElement, IAccessPointOwner {

    private String autoBind;
    private String logHandler;
    private String unbindOnMatch;
    private String consumeOnMatch;





    private carnot_IEventHandlerOwner carnot_ieventhandlerowner;


    public carnot_EventHandlerType(
        String autoBind,        String logHandler,        String unbindOnMatch,        String consumeOnMatch    ) {
        super(
        );
        this.autoBind = autoBind;
        this.logHandler = logHandler;
        this.unbindOnMatch = unbindOnMatch;
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

    public carnot_IEventHandlerOwner getCarnot_ieventhandlerowner() {
        return carnot_ieventhandlerowner;
    }

    public void setCarnot_ieventhandlerowner(carnot_IEventHandlerOwner carnot_ieventhandlerowner) {
        this.carnot_ieventhandlerowner = carnot_ieventhandlerowner;
    }

}