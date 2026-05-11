





import java.util.List;
import java.util.ArrayList;

public class mdc_State  {

    private String input;
    private String name;
    private String messages;





    private mdc_Chatbot mdc_chatbot;




    private mdc_StationaryState mdc_stationarystate;


    public mdc_State(
        String input,        String name,        String messages    ) {
        this.input = input;
        this.name = name;
        this.messages = messages;
    }


    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMessages() {
        return messages;
    }

    public void setMessages(String messages) {
        this.messages = messages;
    }

    public mdc_Chatbot getMdc_chatbot() {
        return mdc_chatbot;
    }

    public void setMdc_chatbot(mdc_Chatbot mdc_chatbot) {
        this.mdc_chatbot = mdc_chatbot;
    }
    public mdc_StationaryState getMdc_stationarystate() {
        return mdc_stationarystate;
    }

    public void setMdc_stationarystate(mdc_StationaryState mdc_stationarystate) {
        this.mdc_stationarystate = mdc_stationarystate;
    }

}