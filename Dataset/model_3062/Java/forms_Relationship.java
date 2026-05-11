





import java.util.List;
import java.util.ArrayList;

public class forms_Relationship  {

    private String name;
    private int lowerBound;
    private int upperBound;





    private forms_Entity forms_entity;




    private forms_Relationship forms_relationship;




    private forms_Entity forms_entity;


    public forms_Relationship(
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
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}