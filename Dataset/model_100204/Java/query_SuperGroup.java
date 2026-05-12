





import java.util.List;
import java.util.ArrayList;

public class query_SuperGroup extends Grouping {

    private String superGroupType;





    private query_SuperGroupElement query_supergroupelement;




    private List<query_SuperGroupElement> query_supergroupelements;


    public query_SuperGroup(
        String superGroupType    ) {
        super(
        );
        this.superGroupType = superGroupType;
        this.query_supergroupelements = new ArrayList<>();
    }

    public query_SuperGroup(
        String superGroupType        ArrayList<query_SuperGroupElement> query_supergroupelements    ) {
        this.superGroupType = superGroupType;
        this.query_supergroupelements = query_supergroupelements;
    }

    public String getSupergrouptype() {
        return superGroupType;
    }

    public void setSupergrouptype(String superGroupType) {
        this.superGroupType = superGroupType;
    }

    public query_SuperGroupElement getQuery_supergroupelement() {
        return query_supergroupelement;
    }

    public void setQuery_supergroupelement(query_SuperGroupElement query_supergroupelement) {
        this.query_supergroupelement = query_supergroupelement;
    }
    public List<query_SuperGroupElement> getQuery_supergroupelements() {
        return query_supergroupelements;
    }

    public void addQuery_supergroupelement(Query_supergroupelement query_supergroupelement) {
        this.query_supergroupelements.add(query_supergroupelement);
    }

}