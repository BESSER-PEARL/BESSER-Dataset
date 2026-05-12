





import java.util.List;
import java.util.ArrayList;

public class requirements_RelationShip extends BasicElement {

    private int targetMax;
    private int sourceMax;
    private int sourceMin;
    private int targetMin;





    private requirements_Entity requirements_entity;




    private requirements_Entity requirements_entity;


    public requirements_RelationShip(
        int targetMax,        int sourceMax,        int sourceMin,        int targetMin    ) {
        super(
        );
        this.targetMax = targetMax;
        this.sourceMax = sourceMax;
        this.sourceMin = sourceMin;
        this.targetMin = targetMin;
    }


    public int getTargetmax() {
        return targetMax;
    }

    public void setTargetmax(int targetMax) {
        this.targetMax = targetMax;
    }
    public int getSourcemax() {
        return sourceMax;
    }

    public void setSourcemax(int sourceMax) {
        this.sourceMax = sourceMax;
    }
    public int getSourcemin() {
        return sourceMin;
    }

    public void setSourcemin(int sourceMin) {
        this.sourceMin = sourceMin;
    }
    public int getTargetmin() {
        return targetMin;
    }

    public void setTargetmin(int targetMin) {
        this.targetMin = targetMin;
    }

    public requirements_Entity getRequirements_entity() {
        return requirements_entity;
    }

    public void setRequirements_entity(requirements_Entity requirements_entity) {
        this.requirements_entity = requirements_entity;
    }
    public requirements_Entity getRequirements_entity() {
        return requirements_entity;
    }

    public void setRequirements_entity(requirements_Entity requirements_entity) {
        this.requirements_entity = requirements_entity;
    }

}