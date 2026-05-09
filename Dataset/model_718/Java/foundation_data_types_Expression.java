





import java.util.List;
import java.util.ArrayList;

public class foundation_data_types_Expression  {

    private String language;
    private String body;



    public foundation_data_types_Expression(
        String language,        String body    ) {
        this.language = language;
        this.body = body;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}