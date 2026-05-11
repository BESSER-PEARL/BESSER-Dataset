





import java.util.List;
import java.util.ArrayList;

public class cmof_Class extends Classifier {

    private boolean isAbstract;





    private List<cmof_Operation> cmof_operations;




    private cmof_Property cmof_property;




    private List<cmof_Class> cmof_classs;




    private List<cmof_Property> cmof_propertys;




    private cmof_Operation cmof_operation;


    public cmof_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.cmof_operations = new ArrayList<>();
        this.cmof_classs = new ArrayList<>();
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Class(
        boolean isAbstract        ArrayList<cmof_Operation> cmof_operations,        ArrayList<cmof_Class> cmof_classs,        ArrayList<cmof_Property> cmof_propertys    ) {
        this.isAbstract = isAbstract;
        this.cmof_operations = cmof_operations;
        this.cmof_classs = cmof_classs;
        this.cmof_propertys = cmof_propertys;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
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
    public List<cmof_Class> getCmof_classs() {
        return cmof_classs;
    }

    public void addCmof_class(Cmof_class cmof_class) {
        this.cmof_classs.add(cmof_class);
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public cmof_Operation getCmof_operation() {
        return cmof_operation;
    }

    public void setCmof_operation(cmof_Operation cmof_operation) {
        this.cmof_operation = cmof_operation;
    }

}