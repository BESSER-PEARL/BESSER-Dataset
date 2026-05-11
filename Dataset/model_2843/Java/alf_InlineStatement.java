





import java.util.List;
import java.util.ArrayList;

public class alf_InlineStatement extends Statement {

    private String langageName;
    private String body;



    public alf_InlineStatement(
        String langageName,        String body    ) {
        super(
        );
        this.langageName = langageName;
        this.body = body;
    }


    public String getLangagename() {
        return langageName;
    }

    public void setLangagename(String langageName) {
        this.langageName = langageName;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}