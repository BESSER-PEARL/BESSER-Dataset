





import java.util.List;
import java.util.ArrayList;

public class umlTransition_AnyReceiveEventRule extends EventRule {

    private String isAReceiveEvent;



    public umlTransition_AnyReceiveEventRule(
        String isAReceiveEvent    ) {
        super(
        );
        this.isAReceiveEvent = isAReceiveEvent;
    }


    public String getIsareceiveevent() {
        return isAReceiveEvent;
    }

    public void setIsareceiveevent(String isAReceiveEvent) {
        this.isAReceiveEvent = isAReceiveEvent;
    }


}