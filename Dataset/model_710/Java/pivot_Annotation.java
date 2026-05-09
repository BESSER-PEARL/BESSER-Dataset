





import java.util.List;
import java.util.ArrayList;

public class pivot_Annotation extends NamedElement {






    private List<pivot_Detail> pivot_details;


    public pivot_Annotation(
    ) {
        super(
        );
        this.pivot_details = new ArrayList<>();
    }

    public pivot_Annotation(
        ArrayList<pivot_Detail> pivot_details    ) {
        this.pivot_details = pivot_details;
    }


    public List<pivot_Detail> getPivot_details() {
        return pivot_details;
    }

    public void addPivot_detail(Pivot_detail pivot_detail) {
        this.pivot_details.add(pivot_detail);
    }

}