





import java.util.List;
import java.util.ArrayList;

public class emof_NamedElement extends Element {

    private String name;



    public emof_NamedElement(
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