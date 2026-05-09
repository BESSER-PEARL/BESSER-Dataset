





import java.util.List;
import java.util.ArrayList;

public class basecs_TupleTypeCS extends TypedRefCS, Nameable {

    private String name;



    public basecs_TupleTypeCS(
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