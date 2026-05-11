





import java.util.List;
import java.util.ArrayList;

public class namespace_XMLNamespaceDocumentRoot  {

    private String space;
    private String lang;
    private String base;
    private String id;
    private String mixed;



    public namespace_XMLNamespaceDocumentRoot(
        String space,        String lang,        String base,        String id,        String mixed    ) {
        this.space = space;
        this.lang = lang;
        this.base = base;
        this.id = id;
        this.mixed = mixed;
    }


    public String getSpace() {
        return space;
    }

    public void setSpace(String space) {
        this.space = space;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getBase() {
        return base;
    }

    public void setBase(String base) {
        this.base = base;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}