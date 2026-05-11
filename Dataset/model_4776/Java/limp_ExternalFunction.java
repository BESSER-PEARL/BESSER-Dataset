





import java.util.List;
import java.util.ArrayList;

public class limp_ExternalFunction extends Declaration, FunctionRef {

    private String name;



    public limp_ExternalFunction(
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