





import java.util.List;
import java.util.ArrayList;

public class model_Documentation extends BPELExtensibleElement {

    private String source;
    private String lang;
    private String value;



    public model_Documentation(
        String source,        String lang,        String value    ) {
        super(
        );
        this.source = source;
        this.lang = lang;
        this.value = value;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}