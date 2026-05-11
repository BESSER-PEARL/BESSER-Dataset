





import java.util.List;
import java.util.ArrayList;

public class co2_IntSum extends Contract {






    private List<co2_IntAction> co2_intactions;


    public co2_IntSum(
    ) {
        super(
        );
        this.co2_intactions = new ArrayList<>();
    }

    public co2_IntSum(
        ArrayList<co2_IntAction> co2_intactions    ) {
        this.co2_intactions = co2_intactions;
    }


    public List<co2_IntAction> getCo2_intactions() {
        return co2_intactions;
    }

    public void addCo2_intaction(Co2_intaction co2_intaction) {
        this.co2_intactions.add(co2_intaction);
    }

}