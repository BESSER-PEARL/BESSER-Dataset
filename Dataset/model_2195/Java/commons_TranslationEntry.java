





import java.util.List;
import java.util.ArrayList;

public class commons_TranslationEntry  {

    private String key;





    private commons_Translatable commons_translatable;


    public commons_TranslationEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public commons_Translatable getCommons_translatable() {
        return commons_translatable;
    }

    public void setCommons_translatable(commons_Translatable commons_translatable) {
        this.commons_translatable = commons_translatable;
    }

}