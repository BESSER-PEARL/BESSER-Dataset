





import java.util.List;
import java.util.ArrayList;

public class commons_NamedElement extends Commentable {

    private String name;



    public commons_NamedElement(
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