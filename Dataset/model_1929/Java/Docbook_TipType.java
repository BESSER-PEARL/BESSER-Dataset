





import java.util.List;
import java.util.ArrayList;

public class Docbook_TipType  {

    private String mixed;





    private Docbook_PrefaceType docbook_prefacetype;




    private Docbook_SectionType docbook_sectiontype;




    private Docbook_DocumentRoot docbook_documentroot;


    public Docbook_TipType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_PrefaceType getDocbook_prefacetype() {
        return docbook_prefacetype;
    }

    public void setDocbook_prefacetype(Docbook_PrefaceType docbook_prefacetype) {
        this.docbook_prefacetype = docbook_prefacetype;
    }
    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }

}