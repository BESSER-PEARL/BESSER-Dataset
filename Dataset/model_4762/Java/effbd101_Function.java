





import java.util.List;
import java.util.ArrayList;

public class effbd101_Function extends SequenceNode, ProcessNode {






    private List<effbd101_Function> effbd101_functions;


    public effbd101_Function(
    ) {
        super(
        );
        this.effbd101_functions = new ArrayList<>();
    }

    public effbd101_Function(
        ArrayList<effbd101_Function> effbd101_functions    ) {
        this.effbd101_functions = effbd101_functions;
    }


    public List<effbd101_Function> getEffbd101_functions() {
        return effbd101_functions;
    }

    public void addEffbd101_function(Effbd101_function effbd101_function) {
        this.effbd101_functions.add(effbd101_function);
    }

}