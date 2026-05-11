





import java.util.List;
import java.util.ArrayList;

public class cmof_DataType extends Classifier {






    private cmof_Property cmof_property;




    private List<cmof_Property> cmof_propertys;


    public cmof_DataType(
    ) {
        super(
        );
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_DataType(
        ArrayList<cmof_Property> cmof_propertys    ) {
        this.cmof_propertys = cmof_propertys;
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

}