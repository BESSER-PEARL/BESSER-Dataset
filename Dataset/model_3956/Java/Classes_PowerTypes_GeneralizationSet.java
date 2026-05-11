





import java.util.List;
import java.util.ArrayList;

public class Classes_PowerTypes_GeneralizationSet extends PackageableElement {

    private boolean isDisjoint;
    private boolean isCovering;



    public Classes_PowerTypes_GeneralizationSet(
        boolean isDisjoint,        boolean isCovering    ) {
        super(
        );
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
    }


    public boolean getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(boolean isDisjoint) {
        this.isDisjoint = isDisjoint;
    }
    public boolean getIscovering() {
        return isCovering;
    }

    public void setIscovering(boolean isCovering) {
        this.isCovering = isCovering;
    }


}