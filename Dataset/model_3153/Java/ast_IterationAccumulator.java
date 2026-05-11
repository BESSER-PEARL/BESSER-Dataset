





import java.util.List;
import java.util.ArrayList;

public class ast_IterationAccumulator extends CallableElement {

    private String name;



    public ast_IterationAccumulator(
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