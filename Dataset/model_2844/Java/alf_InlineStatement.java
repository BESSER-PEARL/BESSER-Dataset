





import java.util.List;
import java.util.ArrayList;

public class alf_InlineStatement extends Statement {

    private String body;
    private String langageName;



    public alf_InlineStatement(
        String body,        String langageName    ) {
        super(
        );
        this.body = body;
        this.langageName = langageName;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getLangagename() {
        return langageName;
    }

    public void setLangagename(String langageName) {
        this.langageName = langageName;
    }


}