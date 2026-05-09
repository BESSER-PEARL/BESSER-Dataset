





import java.util.List;
import java.util.ArrayList;

public class pivot_Profile extends Package {






    private List<pivot_ProfileApplication> pivot_profileapplications;




    private pivot_ProfileApplication pivot_profileapplication;


    public pivot_Profile(
    ) {
        super(
        );
        this.pivot_profileapplications = new ArrayList<>();
    }

    public pivot_Profile(
        ArrayList<pivot_ProfileApplication> pivot_profileapplications    ) {
        this.pivot_profileapplications = pivot_profileapplications;
    }


    public List<pivot_ProfileApplication> getPivot_profileapplications() {
        return pivot_profileapplications;
    }

    public void addPivot_profileapplication(Pivot_profileapplication pivot_profileapplication) {
        this.pivot_profileapplications.add(pivot_profileapplication);
    }
    public pivot_ProfileApplication getPivot_profileapplication() {
        return pivot_profileapplication;
    }

    public void setPivot_profileapplication(pivot_ProfileApplication pivot_profileapplication) {
        this.pivot_profileapplication = pivot_profileapplication;
    }

}