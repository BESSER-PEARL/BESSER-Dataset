





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_ModelElementQueue extends QoolQueue {






    private List<ClassUse> classuses;




    private ClassUse classuse;


    public frontend_qool_ModelElementQueue(
    ) {
        super(
        );
        this.classuses = new ArrayList<>();
    }

    public frontend_qool_ModelElementQueue(
        ArrayList<ClassUse> classuses    ) {
        this.classuses = classuses;
    }


    public List<ClassUse> getClassuses() {
        return classuses;
    }

    public void addClassuse(Classuse classuse) {
        this.classuses.add(classuse);
    }
    public ClassUse getClassuse() {
        return classuse;
    }

    public void setClassuse(ClassUse classuse) {
        this.classuse = classuse;
    }

}