





import java.util.List;
import java.util.ArrayList;

public class OO_Feature extends NamedElement {

    private String visibility;



    public OO_Feature(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}