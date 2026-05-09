





import java.util.List;
import java.util.ArrayList;

public class Docbook_KeywordsetType  {

    private String keyword;





    private Docbook_InfoType docbook_infotype;




    private Docbook_DocumentRoot docbook_documentroot;


    public Docbook_KeywordsetType(
        String keyword    ) {
        this.keyword = keyword;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }

}