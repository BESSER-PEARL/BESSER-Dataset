





import java.util.List;
import java.util.ArrayList;

public class UML2_PackageImport extends DirectedRelationship {

    private String visibility;



    public UML2_PackageImport(
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