





import java.util.List;
import java.util.ArrayList;

public class forms_Relationship  {

    private String name;
    private String lowerBound;
    private String upperBound;





    private forms_Relationship forms_relationship;




    private forms_Entity forms_entity;




    private forms_Entity forms_entity;


    public forms_Relationship(
        String name,        String lowerBound,        String upperBound    ) {
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
    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
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
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}