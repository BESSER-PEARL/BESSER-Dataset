





import java.util.List;
import java.util.ArrayList;

public class cmof_Class extends Classifier {

    private boolean isAbstract;





    private cmof_Property cmof_property;




    private List<cmof_Property> cmof_propertys;




    private cmof_Class cmof_class;


    public cmof_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Class(
        boolean isAbstract        ArrayList<cmof_Property> cmof_propertys    ) {
        this.isAbstract = isAbstract;
        this.cmof_propertys = cmof_propertys;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
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
    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }

}