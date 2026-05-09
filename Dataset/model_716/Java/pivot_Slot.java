





import java.util.List;
import java.util.ArrayList;

public class pivot_Slot extends Element {






    private pivot_InstanceSpecification pivot_instancespecification;




    private pivot_Property pivot_property;




    private List<pivot_ValueSpecification> pivot_valuespecifications;




    private pivot_InstanceSpecification pivot_instancespecification;


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


    public pivot_InstanceSpecification getPivot_instancespecification() {
        return pivot_instancespecification;
    }

    public void setPivot_instancespecification(pivot_InstanceSpecification pivot_instancespecification) {
        this.pivot_instancespecification = pivot_instancespecification;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public List<pivot_ValueSpecification> getPivot_valuespecifications() {
        return pivot_valuespecifications;
    }

    public void addPivot_valuespecification(Pivot_valuespecification pivot_valuespecification) {
        this.pivot_valuespecifications.add(pivot_valuespecification);
    }
    public pivot_InstanceSpecification getPivot_instancespecification() {
        return pivot_instancespecification;
    }

    public void setPivot_instancespecification(pivot_InstanceSpecification pivot_instancespecification) {
        this.pivot_instancespecification = pivot_instancespecification;
    }

}