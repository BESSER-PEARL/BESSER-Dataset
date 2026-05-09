





import java.util.List;
import java.util.ArrayList;

public class Docbook_LegalNoticeType  {

    private String group;





    private Docbook_InfoType docbook_infotype;




    private List<Docbook_ParaType> docbook_paratypes;




    private List<Docbook_OrderedlistType> docbook_orderedlisttypes;




    private Docbook_TitleType docbook_titletype;


    public Docbook_LegalNoticeType(
        String group    ) {
        this.group = group;
        this.docbook_paratypes = new ArrayList<>();
        this.docbook_orderedlisttypes = new ArrayList<>();
    }

    public Docbook_LegalNoticeType(
        String group        ArrayList<Docbook_ParaType> docbook_paratypes,        ArrayList<Docbook_OrderedlistType> docbook_orderedlisttypes    ) {
        this.group = group;
        this.docbook_paratypes = docbook_paratypes;
        this.docbook_orderedlisttypes = docbook_orderedlisttypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }
    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }
    public List<Docbook_OrderedlistType> getDocbook_orderedlisttypes() {
        return docbook_orderedlisttypes;
    }

    public void addDocbook_orderedlisttype(Docbook_orderedlisttype docbook_orderedlisttype) {
        this.docbook_orderedlisttypes.add(docbook_orderedlisttype);
    }
    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }

}