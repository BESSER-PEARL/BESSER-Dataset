





import java.util.List;
import java.util.ArrayList;

public class Docbook_FigureType  {

    private String id;
    private String float;





    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_TitleType docbook_titletype;




    private Docbook_SectionType docbook_sectiontype;


    public Docbook_FigureType(
        String id,        String float    ) {
        this.id = id;
        this.float = float;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFloat() {
        return float;
    }

    public void setFloat(String float) {
        this.float = float;
    }

    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }
    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }

}