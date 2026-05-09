





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ReplyAction extends Action {

    private String replyToCall;



    public UMLModel_ReplyAction(
        String replyToCall    ) {
        super(
        );
        this.replyToCall = replyToCall;
    }


    public String getReplytocall() {
        return replyToCall;
    }

    public void setReplytocall(String replyToCall) {
        this.replyToCall = replyToCall;
    }


}