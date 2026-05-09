





import java.util.List;
import java.util.ArrayList;

public class Docbook_LinkType  {

    private String linkend;
    private String mixed;
    private String value;





    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_ParaType docbook_paratype;


    public Docbook_LinkType(
        String linkend,        String mixed,        String value    ) {
        this.linkend = linkend;
        this.mixed = mixed;
        this.value = value;
    }


    public String getLinkend() {
        return linkend;
    }

    public void setLinkend(String linkend) {
        this.linkend = linkend;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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
    public Docbook_ParaType getDocbook_paratype() {
        return docbook_paratype;
    }

    public void setDocbook_paratype(Docbook_ParaType docbook_paratype) {
        this.docbook_paratype = docbook_paratype;
    }

}