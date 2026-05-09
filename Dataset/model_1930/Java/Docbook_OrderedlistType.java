





import java.util.List;
import java.util.ArrayList;

public class Docbook_OrderedlistType extends ItemizedlistType {

    private String inheritnum;
    private String continuation;





    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_SectionType docbook_sectiontype;


    public Docbook_OrderedlistType(
        String inheritnum,        String continuation    ) {
        super(
        );
        this.inheritnum = inheritnum;
        this.continuation = continuation;
    }


    public String getInheritnum() {
        return inheritnum;
    }

    public void setInheritnum(String inheritnum) {
        this.inheritnum = inheritnum;
    }
    public String getContinuation() {
        return continuation;
    }

    public void setContinuation(String continuation) {
        this.continuation = continuation;
    }

    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }

}