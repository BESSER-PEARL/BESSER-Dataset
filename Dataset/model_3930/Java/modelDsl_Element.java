





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Element extends Annotated {

    private String name;



    public modelDsl_Element(
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