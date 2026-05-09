





import java.util.List;
import java.util.ArrayList;

public class UMLModel_GeneralizationSet extends PackageableElement {

    private String isCovering;
    private String isDisjoint;
    private String generalization;
    private String powerType;



    public UMLModel_GeneralizationSet(
        String isCovering,        String isDisjoint,        String generalization,        String powerType    ) {
        super(
        );
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.generalization = generalization;
        this.powerType = powerType;
    }


    public String getIscovering() {
        return isCovering;
    }

    public void setIscovering(String isCovering) {
        this.isCovering = isCovering;
    }
    public String getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(String isDisjoint) {
        this.isDisjoint = isDisjoint;
    }
    public String getGeneralization() {
        return generalization;
    }

    public void setGeneralization(String generalization) {
        this.generalization = generalization;
    }
    public String getPowertype() {
        return powerType;
    }

    public void setPowertype(String powerType) {
        this.powerType = powerType;
    }


}