





import java.util.List;
import java.util.ArrayList;

public class genericity_dsl_Metaclass extends LocatedElement {

    private String name;



    public genericity_dsl_Metaclass(
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