





import java.util.List;
import java.util.ArrayList;

public class JTL_emof_Class extends Type {

    private boolean isAbstract;





    private List<Class> classs;




    private List<Operation> operations;


    public JTL_emof_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.classs = new ArrayList<>();
        this.operations = new ArrayList<>();
    }

    public JTL_emof_Class(
        boolean isAbstract        ArrayList<Class> classs,        ArrayList<Operation> operations    ) {
        this.isAbstract = isAbstract;
        this.classs = classs;
        this.operations = operations;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<Class> getClasss() {
        return classs;
    }

    public void addClass(Class class) {
        this.classs.add(class);
    }
    public List<Operation> getOperations() {
        return operations;
    }

    public void addOperation(Operation operation) {
        this.operations.add(operation);
    }

}