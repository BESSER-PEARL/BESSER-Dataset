





import java.util.List;
import java.util.ArrayList;

public class micro_Saga extends NamedElement {






    private List<micro_Step> micro_steps;


    public micro_Saga(
    ) {
        super(
        );
        this.micro_steps = new ArrayList<>();
    }

    public micro_Saga(
        ArrayList<micro_Step> micro_steps    ) {
        this.micro_steps = micro_steps;
    }


    public List<micro_Step> getMicro_steps() {
        return micro_steps;
    }

    public void addMicro_step(Micro_step micro_step) {
        this.micro_steps.add(micro_step);
    }

}