





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentationElement extends IdentifiedElement, DSemanticDecorator, DMappingBased, DRefreshable, DStylizable {

    private String name;



    public viewpoint_DRepresentationElement(
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