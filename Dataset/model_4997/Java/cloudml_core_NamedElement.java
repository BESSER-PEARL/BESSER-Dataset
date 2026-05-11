





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_NamedElement extends CloudMLElement {

    private String name;



    public cloudml_core_NamedElement(
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