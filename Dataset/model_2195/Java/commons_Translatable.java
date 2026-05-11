





import java.util.List;
import java.util.ArrayList;

public class commons_Translatable  {

    private String language;
    private String translationState;
    private String originalLanguage;



    public commons_Translatable(
        String language,        String translationState,        String originalLanguage    ) {
        this.language = language;
        this.translationState = translationState;
        this.originalLanguage = originalLanguage;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getTranslationstate() {
        return translationState;
    }

    public void setTranslationstate(String translationState) {
        this.translationState = translationState;
    }
    public String getOriginallanguage() {
        return originalLanguage;
    }

    public void setOriginallanguage(String originalLanguage) {
        this.originalLanguage = originalLanguage;
    }


}