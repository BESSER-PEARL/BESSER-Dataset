





import java.util.List;
import java.util.ArrayList;

public class micro_Saga extends NamedElement {






    private micro_Data micro_data;




    private micro_Operation micro_operation;




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


    public micro_Data getMicro_data() {
        return micro_data;
    }

    public void setMicro_data(micro_Data micro_data) {
        this.micro_data = micro_data;
    }
    public micro_Operation getMicro_operation() {
        return micro_operation;
    }

    public void setMicro_operation(micro_Operation micro_operation) {
        this.micro_operation = micro_operation;
    }
    public List<micro_Step> getMicro_steps() {
        return micro_steps;
    }

    public void addMicro_step(Micro_step micro_step) {
        this.micro_steps.add(micro_step);
    }

}