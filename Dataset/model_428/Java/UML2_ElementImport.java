





import java.util.List;
import java.util.ArrayList;

public class UML2_ElementImport extends DirectedRelationship {

    private String visibility;



    public UML2_ElementImport(
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