





import java.util.List;
import java.util.ArrayList;

public class xwiki_Link  {

    private String rel;
    private String type;
    private String href;
    private String hrefLang;



    public xwiki_Link(
        String rel,        String type,        String href,        String hrefLang    ) {
        this.rel = rel;
        this.type = type;
        this.href = href;
        this.hrefLang = hrefLang;
    }


    public String getRel() {
        return rel;
    }

    public void setRel(String rel) {
        this.rel = rel;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getHreflang() {
        return hrefLang;
    }

    public void setHreflang(String hrefLang) {
        this.hrefLang = hrefLang;
    }


}