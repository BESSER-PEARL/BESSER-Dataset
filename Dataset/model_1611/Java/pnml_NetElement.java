





import java.util.List;
import java.util.ArrayList;

public class pnml_NetElement extends Element {

    private String name;



    public pnml_NetElement(
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