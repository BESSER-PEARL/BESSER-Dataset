





import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_Relationship  {

    private String name;
    private int lowerBound;
    private int upperBound;





    private Relationship relationship;




    private Entity entity;


    public forms_entityModeling_Relationship(
        String name,        int lowerBound,        int upperBound    ) {
        this.name = name;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public Relationship getRelationship() {
        return relationship;
    }

    public void setRelationship(Relationship relationship) {
        this.relationship = relationship;
    }
    public Entity getEntity() {
        return entity;
    }

    public void setEntity(Entity entity) {
        this.entity = entity;
    }

}