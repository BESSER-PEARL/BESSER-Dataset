





import java.util.List;
import java.util.ArrayList;

public class adlrecurs_Content  {

    private String language;
    private String class_;





    private adlrecurs_AbstractComponent adlrecurs_abstractcomponent;


    public adlrecurs_Content(
        String language,        String class_    ) {
        this.language = language;
        this.class_ = class_;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public adlrecurs_AbstractComponent getAdlrecurs_abstractcomponent() {
        return adlrecurs_abstractcomponent;
    }

    public void setAdlrecurs_abstractcomponent(adlrecurs_AbstractComponent adlrecurs_abstractcomponent) {
        this.adlrecurs_abstractcomponent = adlrecurs_abstractcomponent;
    }

}