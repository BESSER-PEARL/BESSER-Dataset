





import java.util.List;
import java.util.ArrayList;

public class UML2_CallTrigger extends MessageTrigger {






    private UML2_ReplyAction uml2_replyaction;




    private UML2_Operation uml2_operation;


    public UML2_CallTrigger(
    ) {
        super(
        );
    }



    public UML2_ReplyAction getUml2_replyaction() {
        return uml2_replyaction;
    }

    public void setUml2_replyaction(UML2_ReplyAction uml2_replyaction) {
        this.uml2_replyaction = uml2_replyaction;
    }
    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }

}