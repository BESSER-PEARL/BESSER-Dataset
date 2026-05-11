





import java.util.List;
import java.util.ArrayList;

public class commons_TranslationMessageEntry  {

    private String key;
    private String value;





    private commons_Translation commons_translation;


    public commons_TranslationMessageEntry(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public commons_Translation getCommons_translation() {
        return commons_translation;
    }

    public void setCommons_translation(commons_Translation commons_translation) {
        this.commons_translation = commons_translation;
    }

}