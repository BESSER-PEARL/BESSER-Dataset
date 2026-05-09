





import java.util.List;
import java.util.ArrayList;

public class smalluml_NamedElement extends Element {

    private String Name;



    public smalluml_NamedElement(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}