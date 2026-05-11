





import java.util.List;
import java.util.ArrayList;

public class extended_Feature  {

    private int min;
    private String required;
    private int max;
    private String name;





    private extended_Entity extended_entity;




    private extended_AbstractType extended_abstracttype;


    public extended_Feature(
        int min,        String required,        int max,        String name    ) {
        this.min = min;
        this.required = required;
        this.max = max;
        this.name = name;
    }


    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public extended_Entity getExtended_entity() {
        return extended_entity;
    }

    public void setExtended_entity(extended_Entity extended_entity) {
        this.extended_entity = extended_entity;
    }
    public extended_AbstractType getExtended_abstracttype() {
        return extended_abstracttype;
    }

    public void setExtended_abstracttype(extended_AbstractType extended_abstracttype) {
        this.extended_abstracttype = extended_abstracttype;
    }

}