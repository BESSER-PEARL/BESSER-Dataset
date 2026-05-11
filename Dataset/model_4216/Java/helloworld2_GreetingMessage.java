





import java.util.List;
import java.util.ArrayList;

public class helloworld2_GreetingMessage  {

    private String text;





    private helloworld2_Greeting helloworld2_greeting;


    public helloworld2_GreetingMessage(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public helloworld2_Greeting getHelloworld2_greeting() {
        return helloworld2_greeting;
    }

    public void setHelloworld2_greeting(helloworld2_Greeting helloworld2_greeting) {
        this.helloworld2_greeting = helloworld2_greeting;
    }

}