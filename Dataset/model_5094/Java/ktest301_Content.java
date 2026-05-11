





import java.util.List;
import java.util.ArrayList;

public class ktest301_Content  {

    private String language;
    private String class_;





    private ktest301_AbstractComponent ktest301_abstractcomponent;


    public ktest301_Content(
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

    public ktest301_AbstractComponent getKtest301_abstractcomponent() {
        return ktest301_abstractcomponent;
    }

    public void setKtest301_abstractcomponent(ktest301_AbstractComponent ktest301_abstractcomponent) {
        this.ktest301_abstractcomponent = ktest301_abstractcomponent;
    }

}