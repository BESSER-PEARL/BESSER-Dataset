





import java.util.List;
import java.util.ArrayList;

public class pivot_NamedElement extends Nameable, Element {

    private String name;
    private String isStatic;



    public pivot_NamedElement(
        String name,        String isStatic    ) {
        super(
        );
        this.name = name;
        this.isStatic = isStatic;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }


}