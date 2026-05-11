





import java.util.List;
import java.util.ArrayList;

public class limp_LocalFunction extends Declaration, FunctionRef {

    private String name;



    public limp_LocalFunction(
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