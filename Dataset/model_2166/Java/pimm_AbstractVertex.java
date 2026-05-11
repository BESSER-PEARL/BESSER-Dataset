





import java.util.List;
import java.util.ArrayList;

public class pimm_AbstractVertex extends Parameterizable {

    private String name;



    public pimm_AbstractVertex(
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