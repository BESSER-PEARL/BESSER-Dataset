





import java.util.List;
import java.util.ArrayList;

public class UML_14_Feature extends ModelElement {

    private String ownerScope;
    private String visibility;



    public UML_14_Feature(
        String ownerScope,        String visibility    ) {
        super(
        );
        this.ownerScope = ownerScope;
        this.visibility = visibility;
    }


    public String getOwnerscope() {
        return ownerScope;
    }

    public void setOwnerscope(String ownerScope) {
        this.ownerScope = ownerScope;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}