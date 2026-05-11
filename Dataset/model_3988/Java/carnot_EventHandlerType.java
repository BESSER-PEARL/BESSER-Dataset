





import java.util.List;
import java.util.ArrayList;

public class carnot_EventHandlerType extends ITypedElement, IIdentifiableModelElement, IAccessPointOwner {

    private String consumeOnMatch;
    private String logHandler;
    private String autoBind;
    private String unbindOnMatch;



    public carnot_EventHandlerType(
        String consumeOnMatch,        String logHandler,        String autoBind,        String unbindOnMatch    ) {
        super(
        );
        this.consumeOnMatch = consumeOnMatch;
        this.logHandler = logHandler;
        this.autoBind = autoBind;
        this.unbindOnMatch = unbindOnMatch;
    }


    public String getConsumeonmatch() {
        return consumeOnMatch;
    }

    public void setConsumeonmatch(String consumeOnMatch) {
        this.consumeOnMatch = consumeOnMatch;
    }
    public String getLoghandler() {
        return logHandler;
    }

    public void setLoghandler(String logHandler) {
        this.logHandler = logHandler;
    }
    public String getAutobind() {
        return autoBind;
    }

    public void setAutobind(String autoBind) {
        this.autoBind = autoBind;
    }
    public String getUnbindonmatch() {
        return unbindOnMatch;
    }

    public void setUnbindonmatch(String unbindOnMatch) {
        this.unbindOnMatch = unbindOnMatch;
    }


}