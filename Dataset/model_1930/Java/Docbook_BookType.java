





import java.util.List;
import java.util.ArrayList;

public class Docbook_BookType  {

    private String label;
    private String lang;
    private String version;



    public Docbook_BookType(
        String label,        String lang,        String version    ) {
        this.label = label;
        this.lang = lang;
        this.version = version;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}