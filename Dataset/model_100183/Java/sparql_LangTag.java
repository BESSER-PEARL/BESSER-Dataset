





import java.util.List;
import java.util.ArrayList;

public class sparql_LangTag extends RDFTag {

    private String lang;



    public sparql_LangTag(
        String lang    ) {
        super(
        );
        this.lang = lang;
    }


    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }


}