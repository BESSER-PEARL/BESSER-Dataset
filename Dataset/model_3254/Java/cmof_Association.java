





import java.util.List;
import java.util.ArrayList;

public class cmof_Association extends Classifier, Relationship {

    private boolean isDerived;





    private cmof_Property cmof_property;




    private List<cmof_Property> cmof_propertys;




    private List<cmof_Property> cmof_propertys;




    private List<cmof_Property> cmof_propertys;




    private cmof_Property cmof_property;


    public cmof_Association(
        boolean isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.cmof_propertys = new ArrayList<>();
        this.cmof_propertys = new ArrayList<>();
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Association(
        boolean isDerived        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_Property> cmof_propertys    ) {
        this.isDerived = isDerived;
        this.cmof_propertys = cmof_propertys;
        this.cmof_propertys = cmof_propertys;
        this.cmof_propertys = cmof_propertys;
    }

    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }

    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
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