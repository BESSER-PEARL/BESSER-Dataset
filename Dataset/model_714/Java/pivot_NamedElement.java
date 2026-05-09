





import java.util.List;
import java.util.ArrayList;

public class pivot_NamedElement extends Nameable, Element {

    private String isStatic;
    private String name;



    public pivot_NamedElement(
        String isStatic,        String name    ) {
        super(
        );
        this.isStatic = isStatic;
        this.name = name;
    }


    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}