





import java.util.List;
import java.util.ArrayList;

public class pivot_TemplateParameter extends Type {






    private List<pivot_Class> pivot_classs;


    public pivot_TemplateParameter(
    ) {
        super(
        );
        this.pivot_classs = new ArrayList<>();
    }

    public pivot_TemplateParameter(
        ArrayList<pivot_Class> pivot_classs    ) {
        this.pivot_classs = pivot_classs;
    }


    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }

}