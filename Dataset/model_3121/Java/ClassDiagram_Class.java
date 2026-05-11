





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Class extends Classifier {

    private String isAbstract;





    private List<Class> classs;


    public ClassDiagram_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.classs = new ArrayList<>();
    }

    public ClassDiagram_Class(
        String isAbstract        ArrayList<Class> classs    ) {
        this.isAbstract = isAbstract;
        this.classs = classs;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<Class> getClasss() {
        return classs;
    }

    public void addClass(Class class) {
        this.classs.add(class);
    }

}