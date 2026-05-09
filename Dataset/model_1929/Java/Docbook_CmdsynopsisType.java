





import java.util.List;
import java.util.ArrayList;

public class Docbook_CmdsynopsisType  {






    private Docbook_SectionType docbook_sectiontype;




    private List<Docbook_ArgType> docbook_argtypes;


    public Docbook_CmdsynopsisType(
    ) {
        this.docbook_argtypes = new ArrayList<>();
    }

    public Docbook_CmdsynopsisType(
        ArrayList<Docbook_ArgType> docbook_argtypes    ) {
        this.docbook_argtypes = docbook_argtypes;
    }


    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }
    public List<Docbook_ArgType> getDocbook_argtypes() {
        return docbook_argtypes;
    }

    public void addDocbook_argtype(Docbook_argtype docbook_argtype) {
        this.docbook_argtypes.add(docbook_argtype);
    }

}