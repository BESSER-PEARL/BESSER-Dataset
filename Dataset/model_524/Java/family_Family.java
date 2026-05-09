





import java.util.List;
import java.util.ArrayList;

public class family_Family extends EModelElement {

    private String name;





    private family_Family family_family;


    public family_Family(
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

    public family_Family getFamily_family() {
        return family_family;
    }

    public void setFamily_family(family_Family family_family) {
        this.family_family = family_family;
    }

}