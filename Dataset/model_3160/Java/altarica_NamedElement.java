





import java.util.List;
import java.util.ArrayList;

public class altarica_NamedElement extends Declaration, AbstractDeclaration {

    private String name;



    public altarica_NamedElement(
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