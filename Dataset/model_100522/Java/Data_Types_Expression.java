





import java.util.List;
import java.util.ArrayList;

public class Data_Types_Expression  {

    private String body;
    private String language;



    public Data_Types_Expression(
        String body,        String language    ) {
        this.body = body;
        this.language = language;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}