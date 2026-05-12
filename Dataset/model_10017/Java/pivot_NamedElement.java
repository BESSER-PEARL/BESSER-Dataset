





import java.util.List;
import java.util.ArrayList;

public class pivot_NamedElement extends Nameable, Element {

    private String name;



    public pivot_NamedElement(
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