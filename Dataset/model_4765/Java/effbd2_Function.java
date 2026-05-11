





import java.util.List;
import java.util.ArrayList;

public class effbd2_Function extends FunctionSpecification {






    private List<effbd2_Function> effbd2_functions;


    public effbd2_Function(
    ) {
        super(
        );
        this.effbd2_functions = new ArrayList<>();
    }

    public effbd2_Function(
        ArrayList<effbd2_Function> effbd2_functions    ) {
        this.effbd2_functions = effbd2_functions;
    }


    public List<effbd2_Function> getEffbd2_functions() {
        return effbd2_functions;
    }

    public void addEffbd2_function(Effbd2_function effbd2_function) {
        this.effbd2_functions.add(effbd2_function);
    }

}