





import java.util.List;
import java.util.ArrayList;

public class message_Language  {

    private String uid;
    private String lang;
    private String code;
    private boolean defaultLang;



    public message_Language(
        String uid,        String lang,        String code,        boolean defaultLang    ) {
        this.uid = uid;
        this.lang = lang;
        this.code = code;
        this.defaultLang = defaultLang;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public boolean getDefaultlang() {
        return defaultLang;
    }

    public void setDefaultlang(boolean defaultLang) {
        this.defaultLang = defaultLang;
    }


}