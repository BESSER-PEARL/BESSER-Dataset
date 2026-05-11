





import java.util.List;
import java.util.ArrayList;

public class wikidb116_l10n_cache  {

    private String lc_key;
    private String lc_lang;
    private String lc_value;



    public wikidb116_l10n_cache(
        String lc_key,        String lc_lang,        String lc_value    ) {
        this.lc_key = lc_key;
        this.lc_lang = lc_lang;
        this.lc_value = lc_value;
    }


    public String getLc_key() {
        return lc_key;
    }

    public void setLc_key(String lc_key) {
        this.lc_key = lc_key;
    }
    public String getLc_lang() {
        return lc_lang;
    }

    public void setLc_lang(String lc_lang) {
        this.lc_lang = lc_lang;
    }
    public String getLc_value() {
        return lc_value;
    }

    public void setLc_value(String lc_value) {
        this.lc_value = lc_value;
    }


}