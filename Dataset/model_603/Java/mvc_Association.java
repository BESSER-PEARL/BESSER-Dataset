





import java.util.List;
import java.util.ArrayList;

public class mvc_Association extends Annotable {

    private int upperBound;
    private int lowerBound;
    private String name;
    private boolean containment;
    private String type;





    private mvc_Entity mvc_entity;




    private mvc_Entity mvc_entity;




    private mvc_Model mvc_model;


    public mvc_Association(
        int upperBound,        int lowerBound,        String name,        boolean containment,        String type    ) {
        super(
        );
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
        this.name = name;
        this.containment = containment;
        this.type = type;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public mvc_Entity getMvc_entity() {
        return mvc_entity;
    }

    public void setMvc_entity(mvc_Entity mvc_entity) {
        this.mvc_entity = mvc_entity;
    }
    public mvc_Entity getMvc_entity() {
        return mvc_entity;
    }

    public void setMvc_entity(mvc_Entity mvc_entity) {
        this.mvc_entity = mvc_entity;
    }
    public mvc_Model getMvc_model() {
        return mvc_model;
    }

    public void setMvc_model(mvc_Model mvc_model) {
        this.mvc_model = mvc_model;
    }

}