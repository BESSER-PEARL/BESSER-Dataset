





import java.util.List;
import java.util.ArrayList;

public class stateMachine_SMS  {

    private String from_;
    private String to;
    private String text;





    private stateMachine_SendSms statemachine_sendsms;


    public stateMachine_SMS(
        String from_,        String to,        String text    ) {
        this.from_ = from_;
        this.to = to;
        this.text = text;
    }


    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public stateMachine_SendSms getStatemachine_sendsms() {
        return statemachine_sendsms;
    }

    public void setStatemachine_sendsms(stateMachine_SendSms statemachine_sendsms) {
        this.statemachine_sendsms = statemachine_sendsms;
    }

}