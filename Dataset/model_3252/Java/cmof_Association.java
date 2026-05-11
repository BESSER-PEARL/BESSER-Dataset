





import java.util.List;
import java.util.ArrayList;

public class cmof_Association extends Classifier, Relationship {

    private String isDerived;





    private List<cmof_Property> cmof_propertys;




    private cmof_Property cmof_property;




    private cmof_Link cmof_link;




    private List<cmof_Property> cmof_propertys;




    private List<cmof_Property> cmof_propertys;




    private cmof_Property cmof_property;


    public cmof_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.cmof_propertys = new ArrayList<>();
        this.cmof_propertys = new ArrayList<>();
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Association(
        String isDerived        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_Property> cmof_propertys    ) {
        this.isDerived = isDerived;
        this.cmof_propertys = cmof_propertys;
        this.cmof_propertys = cmof_propertys;
        this.cmof_propertys = cmof_propertys;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }
    public cmof_Link getCmof_link() {
        return cmof_link;
    }

    public void setCmof_link(cmof_Link cmof_link) {
        this.cmof_link = cmof_link;
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }

}