





import java.util.List;
import java.util.ArrayList;

public class Docbook_FuncsynopsisType  {






    private List<Docbook_FuncprototypeType> docbook_funcprototypetypes;




    private Docbook_SectionType docbook_sectiontype;


    public Docbook_FuncsynopsisType(
    ) {
        this.docbook_funcprototypetypes = new ArrayList<>();
    }

    public Docbook_FuncsynopsisType(
        ArrayList<Docbook_FuncprototypeType> docbook_funcprototypetypes    ) {
        this.docbook_funcprototypetypes = docbook_funcprototypetypes;
    }


    public List<Docbook_FuncprototypeType> getDocbook_funcprototypetypes() {
        return docbook_funcprototypetypes;
    }

    public void addDocbook_funcprototypetype(Docbook_funcprototypetype docbook_funcprototypetype) {
        this.docbook_funcprototypetypes.add(docbook_funcprototypetype);
    }
    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }

}