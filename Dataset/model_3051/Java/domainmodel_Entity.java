





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Entity extends AbstractElement {

    private String name;



    public domainmodel_Entity(
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