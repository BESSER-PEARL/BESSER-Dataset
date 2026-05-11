





import java.util.List;
import java.util.ArrayList;

public class swml_Reference  {

    private int upperBound;
    private String rolename;
    private int lowerBound;





    private swml_Entity swml_entity;




    private swml_Entity swml_entity;




    private swml_Reference swml_reference;


    public swml_Reference(
        int upperBound,        String rolename,        int lowerBound    ) {
        this.upperBound = upperBound;
        this.rolename = rolename;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public String getRolename() {
        return rolename;
    }

    public void setRolename(String rolename) {
        this.rolename = rolename;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
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
    public swml_Reference getSwml_reference() {
        return swml_reference;
    }

    public void setSwml_reference(swml_Reference swml_reference) {
        this.swml_reference = swml_reference;
    }

}