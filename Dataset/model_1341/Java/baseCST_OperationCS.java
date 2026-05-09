





import java.util.List;
import java.util.ArrayList;

public class baseCST_OperationCS extends FeatureCS, TemplateableElementCS {






    private List<baseCST_ConstraintCS> basecst_constraintcss;




    private List<baseCST_TypedRefCS> basecst_typedrefcss;




    private baseCST_ClassCS basecst_classcs;




    private baseCST_ClassCS basecst_classcs;




    private List<baseCST_ConstraintCS> basecst_constraintcss;


    public baseCST_OperationCS(
    ) {
        super(
        );
        this.basecst_constraintcss = new ArrayList<>();
        this.basecst_typedrefcss = new ArrayList<>();
        this.basecst_constraintcss = new ArrayList<>();
    }

    public baseCST_OperationCS(
        ArrayList<baseCST_ConstraintCS> basecst_constraintcss,        ArrayList<baseCST_TypedRefCS> basecst_typedrefcss,        ArrayList<baseCST_ConstraintCS> basecst_constraintcss    ) {
        this.basecst_constraintcss = basecst_constraintcss;
        this.basecst_typedrefcss = basecst_typedrefcss;
        this.basecst_constraintcss = basecst_constraintcss;
    }


    public List<baseCST_ConstraintCS> getBasecst_constraintcss() {
        return basecst_constraintcss;
    }

    public void addBasecst_constraintcs(Basecst_constraintcs basecst_constraintcs) {
        this.basecst_constraintcss.add(basecst_constraintcs);
    }
    public List<baseCST_TypedRefCS> getBasecst_typedrefcss() {
        return basecst_typedrefcss;
    }

    public void addBasecst_typedrefcs(Basecst_typedrefcs basecst_typedrefcs) {
        this.basecst_typedrefcss.add(basecst_typedrefcs);
    }
    public baseCST_ClassCS getBasecst_classcs() {
        return basecst_classcs;
    }

    public void setBasecst_classcs(baseCST_ClassCS basecst_classcs) {
        this.basecst_classcs = basecst_classcs;
    }
    public baseCST_ClassCS getBasecst_classcs() {
        return basecst_classcs;
    }

    public void setBasecst_classcs(baseCST_ClassCS basecst_classcs) {
        this.basecst_classcs = basecst_classcs;
    }
    public List<baseCST_ConstraintCS> getBasecst_constraintcss() {
        return basecst_constraintcss;
    }

    public void addBasecst_constraintcs(Basecst_constraintcs basecst_constraintcs) {
        this.basecst_constraintcss.add(basecst_constraintcs);
    }

}