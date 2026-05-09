





import java.util.List;
import java.util.ArrayList;

public class Docbook_VarListEntryType  {

    private String termlength;
    private String spacing;





    private Docbook_VariableListType docbook_variablelisttype;




    private List<Docbook_TermType> docbook_termtypes;




    private Docbook_ListitemType docbook_listitemtype;


    public Docbook_VarListEntryType(
        String termlength,        String spacing    ) {
        this.termlength = termlength;
        this.spacing = spacing;
        this.docbook_termtypes = new ArrayList<>();
    }

    public Docbook_VarListEntryType(
        String termlength,        String spacing        ArrayList<Docbook_TermType> docbook_termtypes    ) {
        this.termlength = termlength;
        this.spacing = spacing;
        this.docbook_termtypes = docbook_termtypes;
    }

    public String getTermlength() {
        return termlength;
    }

    public void setTermlength(String termlength) {
        this.termlength = termlength;
    }
    public String getSpacing() {
        return spacing;
    }

    public void setSpacing(String spacing) {
        this.spacing = spacing;
    }

    public Docbook_VariableListType getDocbook_variablelisttype() {
        return docbook_variablelisttype;
    }

    public void setDocbook_variablelisttype(Docbook_VariableListType docbook_variablelisttype) {
        this.docbook_variablelisttype = docbook_variablelisttype;
    }
    public List<Docbook_TermType> getDocbook_termtypes() {
        return docbook_termtypes;
    }

    public void addDocbook_termtype(Docbook_termtype docbook_termtype) {
        this.docbook_termtypes.add(docbook_termtype);
    }
    public Docbook_ListitemType getDocbook_listitemtype() {
        return docbook_listitemtype;
    }

    public void setDocbook_listitemtype(Docbook_ListitemType docbook_listitemtype) {
        this.docbook_listitemtype = docbook_listitemtype;
    }

}