





import java.util.List;
import java.util.ArrayList;

public class mdc_Chatbot  {

    private String name;
    private String token;



    public mdc_Chatbot(
        String name,        String token    ) {
        this.name = name;
        this.token = token;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }


}