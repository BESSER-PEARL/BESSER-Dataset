





import java.util.List;
import java.util.ArrayList;

public class mdc_State  {

    private String name;
    private String messages;
    private String input;





    private mdc_Chatbot mdc_chatbot;


    public mdc_State(
        String name,        String messages,        String input    ) {
        this.name = name;
        this.messages = messages;
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
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }

    public mdc_Chatbot getMdc_chatbot() {
        return mdc_chatbot;
    }

    public void setMdc_chatbot(mdc_Chatbot mdc_chatbot) {
        this.mdc_chatbot = mdc_chatbot;
    }

}