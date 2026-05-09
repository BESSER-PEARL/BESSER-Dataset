





import java.util.List;
import java.util.ArrayList;

public class Janus_emof_Class extends Type {

    private boolean isAbstract;





    private List<Class> classs;


    public Janus_emof_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.classs = new ArrayList<>();
    }

    public Janus_emof_Class(
        boolean isAbstract        ArrayList<Class> classs    ) {
        this.isAbstract = isAbstract;
        this.classs = classs;
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

}