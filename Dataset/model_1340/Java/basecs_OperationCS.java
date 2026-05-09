





import java.util.List;
import java.util.ArrayList;

public class basecs_OperationCS extends TemplateableElementCS, FeatureCS {






    private basecs_ClassCS basecs_classcs;




    private basecs_ClassCS basecs_classcs;




    private List<basecs_ConstraintCS> basecs_constraintcss;




    private List<basecs_TypedRefCS> basecs_typedrefcss;




    private List<basecs_ConstraintCS> basecs_constraintcss;


    public basecs_OperationCS(
    ) {
        super(
        );
        this.basecs_constraintcss = new ArrayList<>();
        this.basecs_typedrefcss = new ArrayList<>();
        this.basecs_constraintcss = new ArrayList<>();
    }

    public basecs_OperationCS(
        ArrayList<basecs_ConstraintCS> basecs_constraintcss,        ArrayList<basecs_TypedRefCS> basecs_typedrefcss,        ArrayList<basecs_ConstraintCS> basecs_constraintcss    ) {
        this.basecs_constraintcss = basecs_constraintcss;
        this.basecs_typedrefcss = basecs_typedrefcss;
        this.basecs_constraintcss = basecs_constraintcss;
    }


    public basecs_ClassCS getBasecs_classcs() {
        return basecs_classcs;
    }

    public void setBasecs_classcs(basecs_ClassCS basecs_classcs) {
        this.basecs_classcs = basecs_classcs;
    }
    public basecs_ClassCS getBasecs_classcs() {
        return basecs_classcs;
    }

    public void setBasecs_classcs(basecs_ClassCS basecs_classcs) {
        this.basecs_classcs = basecs_classcs;
    }
    public List<basecs_ConstraintCS> getBasecs_constraintcss() {
        return basecs_constraintcss;
    }

    public void addBasecs_constraintcs(Basecs_constraintcs basecs_constraintcs) {
        this.basecs_constraintcss.add(basecs_constraintcs);
    }
    public List<basecs_TypedRefCS> getBasecs_typedrefcss() {
        return basecs_typedrefcss;
    }

    public void addBasecs_typedrefcs(Basecs_typedrefcs basecs_typedrefcs) {
        this.basecs_typedrefcss.add(basecs_typedrefcs);
    }
    public List<basecs_ConstraintCS> getBasecs_constraintcss() {
        return basecs_constraintcss;
    }

    public void addBasecs_constraintcs(Basecs_constraintcs basecs_constraintcs) {
        this.basecs_constraintcss.add(basecs_constraintcs);
    }

}