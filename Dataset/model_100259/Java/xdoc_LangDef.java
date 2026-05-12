





import java.util.List;
import java.util.ArrayList;

public class xdoc_LangDef  {

    private String name;
    private String keywords;





    private xdoc_Document xdoc_document;


    public xdoc_LangDef(
        String name,        String keywords    ) {
        this.name = name;
        this.keywords = keywords;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public xdoc_Document getXdoc_document() {
        return xdoc_document;
    }

    public void setXdoc_document(xdoc_Document xdoc_document) {
        this.xdoc_document = xdoc_document;
    }

}