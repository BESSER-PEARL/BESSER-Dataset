





import java.util.List;
import java.util.ArrayList;

public class swml_Relationship  {

    private int lowerBound;
    private int upperBound;
    private String role;





    private swml_Entity swml_entity;




    private swml_Entity swml_entity;


    public swml_Relationship(
        int lowerBound,        int upperBound,        String role    ) {
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.role = role;
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
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public swml_Entity getSwml_entity() {
        return swml_entity;
    }

    public void setSwml_entity(swml_Entity swml_entity) {
        this.swml_entity = swml_entity;
    }
    public swml_Entity getSwml_entity() {
        return swml_entity;
    }

    public void setSwml_entity(swml_Entity swml_entity) {
        this.swml_entity = swml_entity;
    }

}