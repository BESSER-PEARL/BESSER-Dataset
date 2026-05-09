





import java.util.List;
import java.util.ArrayList;

public class pivot_Signal extends NamedElement {






    private pivot_SendSignalAction pivot_sendsignalaction;




    private pivot_MessageType pivot_messagetype;


    public pivot_Signal(
    ) {
        super(
        );
    }



    public pivot_SendSignalAction getPivot_sendsignalaction() {
        return pivot_sendsignalaction;
    }

    public void setPivot_sendsignalaction(pivot_SendSignalAction pivot_sendsignalaction) {
        this.pivot_sendsignalaction = pivot_sendsignalaction;
    }
    public pivot_MessageType getPivot_messagetype() {
        return pivot_messagetype;
    }

    public void setPivot_messagetype(pivot_MessageType pivot_messagetype) {
        this.pivot_messagetype = pivot_messagetype;
    }

}