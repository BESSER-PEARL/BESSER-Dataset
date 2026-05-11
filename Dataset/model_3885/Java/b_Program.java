





import java.util.List;
import java.util.ArrayList;

public class b_Program  {






    private List<b_Implementation> b_implementations;




    private List<b_Machine> b_machines;


    public b_Program(
    ) {
        this.b_implementations = new ArrayList<>();
        this.b_machines = new ArrayList<>();
    }

    public b_Program(
        ArrayList<b_Implementation> b_implementations,        ArrayList<b_Machine> b_machines    ) {
        this.b_implementations = b_implementations;
        this.b_machines = b_machines;
    }


    public List<b_Implementation> getB_implementations() {
        return b_implementations;
    }

    public void addB_implementation(B_implementation b_implementation) {
        this.b_implementations.add(b_implementation);
    }
    public List<b_Machine> getB_machines() {
        return b_machines;
    }

    public void addB_machine(B_machine b_machine) {
        this.b_machines.add(b_machine);
    }

}