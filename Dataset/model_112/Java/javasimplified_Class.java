





import java.util.List;
import java.util.ArrayList;

public class javasimplified_Class extends Type {

    private boolean isAbstract;





    private javasimplified_Package javasimplified_package;




    private javasimplified_Class javasimplified_class;




    private javasimplified_Method javasimplified_method;




    private List<javasimplified_Method> javasimplified_methods;


    public javasimplified_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.javasimplified_methods = new ArrayList<>();
    }

    public javasimplified_Class(
        boolean isAbstract        ArrayList<javasimplified_Method> javasimplified_methods    ) {
        this.isAbstract = isAbstract;
        this.javasimplified_methods = javasimplified_methods;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public javasimplified_Package getJavasimplified_package() {
        return javasimplified_package;
    }

    public void setJavasimplified_package(javasimplified_Package javasimplified_package) {
        this.javasimplified_package = javasimplified_package;
    }
    public javasimplified_Class getJavasimplified_class() {
        return javasimplified_class;
    }

    public void setJavasimplified_class(javasimplified_Class javasimplified_class) {
        this.javasimplified_class = javasimplified_class;
    }
    public javasimplified_Method getJavasimplified_method() {
        return javasimplified_method;
    }

    public void setJavasimplified_method(javasimplified_Method javasimplified_method) {
        this.javasimplified_method = javasimplified_method;
    }
    public List<javasimplified_Method> getJavasimplified_methods() {
        return javasimplified_methods;
    }

    public void addJavasimplified_method(Javasimplified_method javasimplified_method) {
        this.javasimplified_methods.add(javasimplified_method);
    }

}