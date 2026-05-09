





import java.util.List;
import java.util.ArrayList;

public class Docbook_RefSect1Type  {

    private String id;
    private String group;





    private Docbook_TitleType docbook_titletype;




    private List<Docbook_ParaType> docbook_paratypes;




    private List<Docbook_VariableListType> docbook_variablelisttypes;




    private Docbook_RefEntryType docbook_refentrytype;


    public Docbook_RefSect1Type(
        String id,        String group    ) {
        this.id = id;
        this.group = group;
        this.docbook_paratypes = new ArrayList<>();
        this.docbook_variablelisttypes = new ArrayList<>();
    }

    public Docbook_RefSect1Type(
        String id,        String group        ArrayList<Docbook_ParaType> docbook_paratypes,        ArrayList<Docbook_VariableListType> docbook_variablelisttypes    ) {
        this.id = id;
        this.group = group;
        this.docbook_paratypes = docbook_paratypes;
        this.docbook_variablelisttypes = docbook_variablelisttypes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }
    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }
    public List<Docbook_VariableListType> getDocbook_variablelisttypes() {
        return docbook_variablelisttypes;
    }

    public void addDocbook_variablelisttype(Docbook_variablelisttype docbook_variablelisttype) {
        this.docbook_variablelisttypes.add(docbook_variablelisttype);
    }
    public Docbook_RefEntryType getDocbook_refentrytype() {
        return docbook_refentrytype;
    }

    public void setDocbook_refentrytype(Docbook_RefEntryType docbook_refentrytype) {
        this.docbook_refentrytype = docbook_refentrytype;
    }

}