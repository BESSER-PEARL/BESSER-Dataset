





import java.util.List;
import java.util.ArrayList;

public class cobol_functions_Argumentable  {






    private List<Argument> arguments;




    private Argument argument;


    public cobol_functions_Argumentable(
    ) {
        this.arguments = new ArrayList<>();
    }

    public cobol_functions_Argumentable(
        ArrayList<Argument> arguments    ) {
        this.arguments = arguments;
    }


    public List<Argument> getArguments() {
        return arguments;
    }

    public void addArgument(Argument argument) {
        this.arguments.add(argument);
    }
    public Argument getArgument() {
        return argument;
    }

    public void setArgument(Argument argument) {
        this.argument = argument;
    }

}