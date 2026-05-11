





import java.util.List;
import java.util.ArrayList;

public class cmof_Class extends Classifier {






    private cmof_Class cmof_class;




    private List<cmof_Property> cmof_propertys;




    private cmof_Element cmof_element;




    private cmof_Property cmof_property;


    public cmof_Class(
    ) {
        super(
        );
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Class(
        ArrayList<cmof_Property> cmof_propertys    ) {
        this.cmof_propertys = cmof_propertys;
    }


    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public cmof_Element getCmof_element() {
        return cmof_element;
    }

    public void setCmof_element(cmof_Element cmof_element) {
        this.cmof_element = cmof_element;
    }
    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }

}