





import java.util.List;
import java.util.ArrayList;

public class statesml_RegularState extends State {






    private List<statesml_Function> statesml_functions;


    public statesml_RegularState(
    ) {
        super(
        );
        this.statesml_functions = new ArrayList<>();
    }

    public statesml_RegularState(
        ArrayList<statesml_Function> statesml_functions    ) {
        this.statesml_functions = statesml_functions;
    }


    public List<statesml_Function> getStatesml_functions() {
        return statesml_functions;
    }

    public void addStatesml_function(Statesml_function statesml_function) {
        this.statesml_functions.add(statesml_function);
    }

}