





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_ValueExpression  {

    private String language;
    private String langName;
    private String body;



    public gmf_all_mappings_ValueExpression(
        String language,        String langName,        String body    ) {
        this.language = language;
        this.langName = langName;
        this.body = body;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getLangname() {
        return langName;
    }

    public void setLangname(String langName) {
        this.langName = langName;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}