





import java.util.List;
import java.util.ArrayList;

public class adl301_Content  {

    private String class_;
    private String language;





    private adl301_AbstractComponent adl301_abstractcomponent;


    public adl301_Content(
        String class_,        String language    ) {
        this.class_ = class_;
        this.language = language;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public adl301_AbstractComponent getAdl301_abstractcomponent() {
        return adl301_abstractcomponent;
    }

    public void setAdl301_abstractcomponent(adl301_AbstractComponent adl301_abstractcomponent) {
        this.adl301_abstractcomponent = adl301_abstractcomponent;
    }

}