





import java.util.List;
import java.util.ArrayList;

public class forms_Relationship extends Feature {

    private int upperBound;
    private int lowerBound;





    private forms_Entity forms_entity;




    private forms_Relationship forms_relationship;


    public forms_Relationship(
        int upperBound,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
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

    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }
    public forms_Relationship getForms_relationship() {
        return forms_relationship;
    }

    public void setForms_relationship(forms_Relationship forms_relationship) {
        this.forms_relationship = forms_relationship;
    }

}