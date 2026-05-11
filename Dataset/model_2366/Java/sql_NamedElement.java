





import java.util.List;
import java.util.ArrayList;

public class sql_NamedElement extends ModelElement {

    private String name;



    public sql_NamedElement(
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