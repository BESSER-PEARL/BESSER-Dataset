





import java.util.List;
import java.util.ArrayList;

public class cmof_DataType extends Classifier {






    private cmof_Operation cmof_operation;




    private List<cmof_Property> cmof_propertys;




    private List<cmof_Operation> cmof_operations;




    private cmof_Property cmof_property;


    public cmof_DataType(
    ) {
        super(
        );
        this.cmof_propertys = new ArrayList<>();
        this.cmof_operations = new ArrayList<>();
    }

    public cmof_DataType(
        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_Operation> cmof_operations    ) {
        this.cmof_propertys = cmof_propertys;
        this.cmof_operations = cmof_operations;
    }


    public cmof_Operation getCmof_operation() {
        return cmof_operation;
    }

    public void setCmof_operation(cmof_Operation cmof_operation) {
        this.cmof_operation = cmof_operation;
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public List<cmof_Operation> getCmof_operations() {
        return cmof_operations;
    }

    public void addCmof_operation(Cmof_operation cmof_operation) {
        this.cmof_operations.add(cmof_operation);
    }
    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }

}