





import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_langlinks  {

    private String ll_from;
    private String ll_lang;
    private String ll_title;



    public wikidb116_version116_langlinks(
        String ll_from,        String ll_lang,        String ll_title    ) {
        this.ll_from = ll_from;
        this.ll_lang = ll_lang;
        this.ll_title = ll_title;
    }


    public String getLl_from() {
        return ll_from;
    }

    public void setLl_from(String ll_from) {
        this.ll_from = ll_from;
    }
    public String getLl_lang() {
        return ll_lang;
    }

    public void setLl_lang(String ll_lang) {
        this.ll_lang = ll_lang;
    }
    public String getLl_title() {
        return ll_title;
    }

    public void setLl_title(String ll_title) {
        this.ll_title = ll_title;
    }


}