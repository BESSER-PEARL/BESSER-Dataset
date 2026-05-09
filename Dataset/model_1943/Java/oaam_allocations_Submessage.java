





import java.util.List;
import java.util.ArrayList;

public class oaam_allocations_Submessage extends MessageA {

    private int position;





    private SubmessageInMessageCapability submessageinmessagecapability;


    public oaam_allocations_Submessage(
        int position    ) {
        super(
        );
        this.position = position;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public SubmessageInMessageCapability getSubmessageinmessagecapability() {
        return submessageinmessagecapability;
    }

    public void setSubmessageinmessagecapability(SubmessageInMessageCapability submessageinmessagecapability) {
        this.submessageinmessagecapability = submessageinmessagecapability;
    }

}