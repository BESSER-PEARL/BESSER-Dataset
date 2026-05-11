





import java.util.List;
import java.util.ArrayList;

public class cmof_Class extends Classifier {






    private cmof_Property cmof_property;




    private List<cmof_Class> cmof_classs;




    private cmof_Element cmof_element;




    private List<cmof_Property> cmof_propertys;


    public cmof_Class(
    ) {
        super(
        );
        this.cmof_classs = new ArrayList<>();
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Class(
        ArrayList<cmof_Class> cmof_classs,        ArrayList<cmof_Property> cmof_propertys    ) {
        this.cmof_classs = cmof_classs;
        this.cmof_propertys = cmof_propertys;
    }


    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }
    public List<cmof_Class> getCmof_classs() {
        return cmof_classs;
    }

    public void addCmof_class(Cmof_class cmof_class) {
        this.cmof_classs.add(cmof_class);
    }
    public cmof_Element getCmof_element() {
        return cmof_element;
    }

    public void setCmof_element(cmof_Element cmof_element) {
        this.cmof_element = cmof_element;
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }

}