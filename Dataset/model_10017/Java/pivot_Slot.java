





import java.util.List;
import java.util.ArrayList;

public class pivot_Slot extends Element {






    private List<pivot_ValueSpecification> pivot_valuespecifications;


    public pivot_Slot(
    ) {
        super(
        );
        this.pivot_valuespecifications = new ArrayList<>();
    }

    public pivot_Slot(
        ArrayList<pivot_ValueSpecification> pivot_valuespecifications    ) {
        this.pivot_valuespecifications = pivot_valuespecifications;
    }


    public List<pivot_ValueSpecification> getPivot_valuespecifications() {
        return pivot_valuespecifications;
    }

    public void addPivot_valuespecification(Pivot_valuespecification pivot_valuespecification) {
        this.pivot_valuespecifications.add(pivot_valuespecification);
    }

}