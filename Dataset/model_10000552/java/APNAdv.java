





import java.util.List;
import java.util.ArrayList;

public class APNAdv  {






    private List<APNModel> apnmodels;


    public APNAdv(
    ) {
        this.apnmodels = new ArrayList<>();
    }

    public APNAdv(
        ArrayList<APNModel> apnmodels    ) {
        this.apnmodels = apnmodels;
    }


    public List<APNModel> getApnmodels() {
        return apnmodels;
    }

    public void addApnmodel(Apnmodel apnmodel) {
        this.apnmodels.add(apnmodel);
    }

}