





import java.util.List;
import java.util.ArrayList;

public class helloworldext_GreetingMessage  {

    private String text;





    private helloworldext_Greeting helloworldext_greeting;


    public helloworldext_GreetingMessage(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public helloworldext_Greeting getHelloworldext_greeting() {
        return helloworldext_greeting;
    }

    public void setHelloworldext_greeting(helloworldext_Greeting helloworldext_greeting) {
        this.helloworldext_greeting = helloworldext_greeting;
    }

}