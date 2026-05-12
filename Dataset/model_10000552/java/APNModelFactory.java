





import java.util.List;
import java.util.ArrayList;

public class APNModelFactory  {






    private List<APNModel> apnmodels;




    private APNProgrammaticModel apnprogrammaticmodel;


    public APNModelFactory(
    ) {
        this.apnmodels = new ArrayList<>();
    }

    public APNModelFactory(
        ArrayList<APNModel> apnmodels    ) {
        this.apnmodels = apnmodels;
    }


    public List<APNModel> getApnmodels() {
        return apnmodels;
    }

    public void addApnmodel(Apnmodel apnmodel) {
        this.apnmodels.add(apnmodel);
    }
    public APNProgrammaticModel getApnprogrammaticmodel() {
        return apnprogrammaticmodel;
    }

    public void setApnprogrammaticmodel(APNProgrammaticModel apnprogrammaticmodel) {
        this.apnprogrammaticmodel = apnprogrammaticmodel;
    }

}