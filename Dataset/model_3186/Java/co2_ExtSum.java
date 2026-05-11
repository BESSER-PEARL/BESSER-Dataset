





import java.util.List;
import java.util.ArrayList;

public class co2_ExtSum extends Contract {






    private List<co2_ExtAction> co2_extactions;


    public co2_ExtSum(
    ) {
        super(
        );
        this.co2_extactions = new ArrayList<>();
    }

    public co2_ExtSum(
        ArrayList<co2_ExtAction> co2_extactions    ) {
        this.co2_extactions = co2_extactions;
    }


    public List<co2_ExtAction> getCo2_extactions() {
        return co2_extactions;
    }

    public void addCo2_extaction(Co2_extaction co2_extaction) {
        this.co2_extactions.add(co2_extaction);
    }

}