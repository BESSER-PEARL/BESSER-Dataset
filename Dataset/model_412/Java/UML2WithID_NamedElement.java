





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_NamedElement extends Element {

    private String visibility;



    public UML2WithID_NamedElement(
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