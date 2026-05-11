





import java.util.List;
import java.util.ArrayList;

public class KM3_ModelElement extends LocatedElement {

    private String name;



    public KM3_ModelElement(
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