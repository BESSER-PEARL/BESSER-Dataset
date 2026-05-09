





import java.util.List;
import java.util.ArrayList;

public class Docbook_LiteralType  {

    private String moreinfo;
    private String value;





    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_NoteType docbook_notetype;




    private Docbook_ParaType docbook_paratype;


    public Docbook_LiteralType(
        String moreinfo,        String value    ) {
        this.moreinfo = moreinfo;
        this.value = value;
    }


    public String getMoreinfo() {
        return moreinfo;
    }

    public void setMoreinfo(String moreinfo) {
        this.moreinfo = moreinfo;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_NoteType getDocbook_notetype() {
        return docbook_notetype;
    }

    public void setDocbook_notetype(Docbook_NoteType docbook_notetype) {
        this.docbook_notetype = docbook_notetype;
    }
    public Docbook_ParaType getDocbook_paratype() {
        return docbook_paratype;
    }

    public void setDocbook_paratype(Docbook_ParaType docbook_paratype) {
        this.docbook_paratype = docbook_paratype;
    }

}