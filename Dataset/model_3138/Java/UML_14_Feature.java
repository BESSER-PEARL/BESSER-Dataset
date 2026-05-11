





import java.util.List;
import java.util.ArrayList;

public class UML_14_Feature extends ModelElement {

    private String visibility;
    private String ownerScope;



    public UML_14_Feature(
        String visibility,        String ownerScope    ) {
        super(
        );
        this.visibility = visibility;
        this.ownerScope = ownerScope;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getOwnerscope() {
        return ownerScope;
    }

    public void setOwnerscope(String ownerScope) {
        this.ownerScope = ownerScope;
    }


}