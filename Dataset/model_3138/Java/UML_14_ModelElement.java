





import java.util.List;
import java.util.ArrayList;

public class UML_14_ModelElement extends Element {

    private String name;



    public UML_14_ModelElement(
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