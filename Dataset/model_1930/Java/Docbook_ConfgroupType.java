





import java.util.List;
import java.util.ArrayList;

public class Docbook_ConfgroupType  {

    private String conftitle;
    private String confnum;
    private String confsponsor;





    private Docbook_InfoType docbook_infotype;




    private Docbook_DocumentRoot docbook_documentroot;


    public Docbook_ConfgroupType(
        String conftitle,        String confnum,        String confsponsor    ) {
        this.conftitle = conftitle;
        this.confnum = confnum;
        this.confsponsor = confsponsor;
    }


    public String getConftitle() {
        return conftitle;
    }

    public void setConftitle(String conftitle) {
        this.conftitle = conftitle;
    }
    public String getConfnum() {
        return confnum;
    }

    public void setConfnum(String confnum) {
        this.confnum = confnum;
    }
    public String getConfsponsor() {
        return confsponsor;
    }

    public void setConfsponsor(String confsponsor) {
        this.confsponsor = confsponsor;
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