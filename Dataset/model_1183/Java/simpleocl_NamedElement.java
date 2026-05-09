





import java.util.List;
import java.util.ArrayList;

public class simpleocl_NamedElement extends LocatedElement {

    private String name;



    public simpleocl_NamedElement(
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