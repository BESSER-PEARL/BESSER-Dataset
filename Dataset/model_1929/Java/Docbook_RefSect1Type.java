





import java.util.List;
import java.util.ArrayList;

public class Docbook_RefSect1Type  {

    private String group;
    private String id;





    private Docbook_RefEntryType docbook_refentrytype;




    private List<Docbook_VariableListType> docbook_variablelisttypes;




    private List<Docbook_ParaType> docbook_paratypes;




    private Docbook_TitleType docbook_titletype;


    public Docbook_RefSect1Type(
        String group,        String id    ) {
        this.group = group;
        this.id = id;
        this.docbook_variablelisttypes = new ArrayList<>();
        this.docbook_paratypes = new ArrayList<>();
    }

    public Docbook_RefSect1Type(
        String group,        String id        ArrayList<Docbook_VariableListType> docbook_variablelisttypes,        ArrayList<Docbook_ParaType> docbook_paratypes    ) {
        this.group = group;
        this.id = id;
        this.docbook_variablelisttypes = docbook_variablelisttypes;
        this.docbook_paratypes = docbook_paratypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Docbook_RefEntryType getDocbook_refentrytype() {
        return docbook_refentrytype;
    }

    public void setDocbook_refentrytype(Docbook_RefEntryType docbook_refentrytype) {
        this.docbook_refentrytype = docbook_refentrytype;
    }
    public List<Docbook_VariableListType> getDocbook_variablelisttypes() {
        return docbook_variablelisttypes;
    }

    public void addDocbook_variablelisttype(Docbook_variablelisttype docbook_variablelisttype) {
        this.docbook_variablelisttypes.add(docbook_variablelisttype);
    }
    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }
    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }

}