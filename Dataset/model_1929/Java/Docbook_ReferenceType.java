





import java.util.List;
import java.util.ArrayList;

public class Docbook_ReferenceType  {

    private String version;





    private Docbook_BookType docbook_booktype;




    private Docbook_InfoType docbook_infotype;


    public Docbook_ReferenceType(
        String version    ) {
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public Docbook_BookType getDocbook_booktype() {
        return docbook_booktype;
    }

    public void setDocbook_booktype(Docbook_BookType docbook_booktype) {
        this.docbook_booktype = docbook_booktype;
    }
    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }

}