





import java.util.List;
import java.util.ArrayList;

public class domain_Relation  {

    private String name;
    private String uid;
    private boolean isTree;





    private domain_DataControl domain_datacontrol;




    private domain_Controls domain_controls;




    private List<domain_Link> domain_links;




    private domain_DataControl domain_datacontrol;


    public domain_Relation(
        String name,        String uid,        boolean isTree    ) {
        this.name = name;
        this.uid = uid;
        this.isTree = isTree;
        this.domain_links = new ArrayList<>();
    }

    public domain_Relation(
        String name,        String uid,        boolean isTree        ArrayList<domain_Link> domain_links    ) {
        this.name = name;
        this.uid = uid;
        this.isTree = isTree;
        this.domain_links = domain_links;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public boolean getIstree() {
        return isTree;
    }

    public void setIstree(boolean isTree) {
        this.isTree = isTree;
    }

    public domain_DataControl getDomain_datacontrol() {
        return domain_datacontrol;
    }

    public void setDomain_datacontrol(domain_DataControl domain_datacontrol) {
        this.domain_datacontrol = domain_datacontrol;
    }
    public domain_Controls getDomain_controls() {
        return domain_controls;
    }

    public void setDomain_controls(domain_Controls domain_controls) {
        this.domain_controls = domain_controls;
    }
    public List<domain_Link> getDomain_links() {
        return domain_links;
    }

    public void addDomain_link(Domain_link domain_link) {
        this.domain_links.add(domain_link);
    }
    public domain_DataControl getDomain_datacontrol() {
        return domain_datacontrol;
    }

    public void setDomain_datacontrol(domain_DataControl domain_datacontrol) {
        this.domain_datacontrol = domain_datacontrol;
    }

}