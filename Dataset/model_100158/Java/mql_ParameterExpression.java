





import java.util.List;
import java.util.ArrayList;

public class mql_ParameterExpression extends Variable {

    private String name;



    public mql_ParameterExpression(
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