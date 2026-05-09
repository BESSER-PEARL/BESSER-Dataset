





import java.util.List;
import java.util.ArrayList;

public class Docbook_RefMetaType  {

    private String manvolnum;





    private Docbook_RefEntryType docbook_refentrytype;


    public Docbook_RefMetaType(
        String manvolnum    ) {
        this.manvolnum = manvolnum;
    }


    public String getManvolnum() {
        return manvolnum;
    }

    public void setManvolnum(String manvolnum) {
        this.manvolnum = manvolnum;
    }

    public Docbook_RefEntryType getDocbook_refentrytype() {
        return docbook_refentrytype;
    }

    public void setDocbook_refentrytype(Docbook_RefEntryType docbook_refentrytype) {
        this.docbook_refentrytype = docbook_refentrytype;
    }

}