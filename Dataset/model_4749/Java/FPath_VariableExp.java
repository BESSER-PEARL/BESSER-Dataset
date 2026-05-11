





import java.util.List;
import java.util.ArrayList;

public class FPath_VariableExp extends Expression {

    private String name;



    public FPath_VariableExp(
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