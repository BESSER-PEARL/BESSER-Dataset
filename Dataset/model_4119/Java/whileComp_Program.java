





import java.util.List;
import java.util.ArrayList;

public class whileComp_Program  {






    private List<whileComp_Function> whilecomp_functions;


    public whileComp_Program(
    ) {
        this.whilecomp_functions = new ArrayList<>();
    }

    public whileComp_Program(
        ArrayList<whileComp_Function> whilecomp_functions    ) {
        this.whilecomp_functions = whilecomp_functions;
    }


    public List<whileComp_Function> getWhilecomp_functions() {
        return whilecomp_functions;
    }

    public void addWhilecomp_function(Whilecomp_function whilecomp_function) {
        this.whilecomp_functions.add(whilecomp_function);
    }

}