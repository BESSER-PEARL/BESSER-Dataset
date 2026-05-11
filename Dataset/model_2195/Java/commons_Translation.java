





import java.util.List;
import java.util.ArrayList;

public class commons_Translation  {

    private String language;





    private commons_TranslationEntry commons_translationentry;


    public commons_Translation(
        String language    ) {
        this.language = language;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public commons_TranslationEntry getCommons_translationentry() {
        return commons_translationentry;
    }

    public void setCommons_translationentry(commons_TranslationEntry commons_translationentry) {
        this.commons_translationentry = commons_translationentry;
    }

}