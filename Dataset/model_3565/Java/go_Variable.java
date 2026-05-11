





import java.util.List;
import java.util.ArrayList;

public class go_Variable extends operationsOne, SwitchCase, Atrib_Aux, Greeting, Expression, OperationsOneEquals {

    private String name;



    public go_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}