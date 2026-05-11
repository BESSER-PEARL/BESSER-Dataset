





import java.util.List;
import java.util.ArrayList;

public class diagram_style_CustomStyleDescription extends NodeStyleDescription {

    private String id;



    public diagram_style_CustomStyleDescription(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}