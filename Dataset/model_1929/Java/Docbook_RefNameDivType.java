





import java.util.List;
import java.util.ArrayList;

public class Docbook_RefNameDivType  {

    private String refpurpose;
    private String refname;
    private String refclass;





    private Docbook_RefEntryType docbook_refentrytype;


    public Docbook_RefNameDivType(
        String refpurpose,        String refname,        String refclass    ) {
        this.refpurpose = refpurpose;
        this.refname = refname;
        this.refclass = refclass;
    }


    public String getRefpurpose() {
        return refpurpose;
    }

    public void setRefpurpose(String refpurpose) {
        this.refpurpose = refpurpose;
    }
    public String getRefname() {
        return refname;
    }

    public void setRefname(String refname) {
        this.refname = refname;
    }
    public String getRefclass() {
        return refclass;
    }

    public void setRefclass(String refclass) {
        this.refclass = refclass;
    }

    public Docbook_RefEntryType getDocbook_refentrytype() {
        return docbook_refentrytype;
    }

    public void setDocbook_refentrytype(Docbook_RefEntryType docbook_refentrytype) {
        this.docbook_refentrytype = docbook_refentrytype;
    }

}