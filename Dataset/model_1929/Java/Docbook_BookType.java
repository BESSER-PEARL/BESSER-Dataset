





import java.util.List;
import java.util.ArrayList;

public class Docbook_BookType  {

    private String lang;
    private String label;
    private String version;



    public Docbook_BookType(
        String lang,        String label,        String version    ) {
        this.lang = lang;
        this.label = label;
        this.version = version;
    }


    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}