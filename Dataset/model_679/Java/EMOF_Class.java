





import java.util.List;
import java.util.ArrayList;

public class EMOF_Class extends Type {

    private String isAbstract;





    private List<Operation> operations;




    private List<Class> classs;


    public EMOF_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.operations = new ArrayList<>();
        this.classs = new ArrayList<>();
    }

    public EMOF_Class(
        String isAbstract        ArrayList<Operation> operations,        ArrayList<Class> classs    ) {
        this.isAbstract = isAbstract;
        this.operations = operations;
        this.classs = classs;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<Operation> getOperations() {
        return operations;
    }

    public void addOperation(Operation operation) {
        this.operations.add(operation);
    }
    public List<Class> getClasss() {
        return classs;
    }

    public void addClass(Class class) {
        this.classs.add(class);
    }

}