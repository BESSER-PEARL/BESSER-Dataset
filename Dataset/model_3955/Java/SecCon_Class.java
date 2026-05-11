





import java.util.List;
import java.util.ArrayList;

public class SecCon_Class extends Type {

    private boolean isAbstract;





    private List<SecCon_Operation> seccon_operations;




    private List<SecCon_Class> seccon_classs;


    public SecCon_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.seccon_operations = new ArrayList<>();
        this.seccon_classs = new ArrayList<>();
    }

    public SecCon_Class(
        boolean isAbstract        ArrayList<SecCon_Operation> seccon_operations,        ArrayList<SecCon_Class> seccon_classs    ) {
        this.isAbstract = isAbstract;
        this.seccon_operations = seccon_operations;
        this.seccon_classs = seccon_classs;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<SecCon_Operation> getSeccon_operations() {
        return seccon_operations;
    }

    public void addSeccon_operation(Seccon_operation seccon_operation) {
        this.seccon_operations.add(seccon_operation);
    }
    public List<SecCon_Class> getSeccon_classs() {
        return seccon_classs;
    }

    public void addSeccon_class(Seccon_class seccon_class) {
        this.seccon_classs.add(seccon_class);
    }

}