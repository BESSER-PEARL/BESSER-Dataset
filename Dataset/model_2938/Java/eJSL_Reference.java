





import java.util.List;
import java.util.ArrayList;

public class eJSL_Reference  {

    private boolean preserve;
    private String upper;
    private String lower;
    private boolean id;





    private List<eJSL_Attribute> ejsl_attributes;




    private eJSL_Entity ejsl_entity;




    private eJSL_Entity ejsl_entity;




    private List<eJSL_Attribute> ejsl_attributes;


    public eJSL_Reference(
        boolean preserve,        String upper,        String lower,        boolean id    ) {
        this.preserve = preserve;
        this.upper = upper;
        this.lower = lower;
        this.id = id;
        this.ejsl_attributes = new ArrayList<>();
        this.ejsl_attributes = new ArrayList<>();
    }

    public eJSL_Reference(
        boolean preserve,        String upper,        String lower,        boolean id        ArrayList<eJSL_Attribute> ejsl_attributes,        ArrayList<eJSL_Attribute> ejsl_attributes    ) {
        this.preserve = preserve;
        this.upper = upper;
        this.lower = lower;
        this.id = id;
        this.ejsl_attributes = ejsl_attributes;
        this.ejsl_attributes = ejsl_attributes;
    }

    public boolean getPreserve() {
        return preserve;
    }

    public void setPreserve(boolean preserve) {
        this.preserve = preserve;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public boolean getId() {
        return id;
    }

    public void setId(boolean id) {
        this.id = id;
    }

    public List<eJSL_Attribute> getEjsl_attributes() {
        return ejsl_attributes;
    }

    public void addEjsl_attribute(Ejsl_attribute ejsl_attribute) {
        this.ejsl_attributes.add(ejsl_attribute);
    }
    public eJSL_Entity getEjsl_entity() {
        return ejsl_entity;
    }

    public void setEjsl_entity(eJSL_Entity ejsl_entity) {
        this.ejsl_entity = ejsl_entity;
    }
    public eJSL_Entity getEjsl_entity() {
        return ejsl_entity;
    }

    public void setEjsl_entity(eJSL_Entity ejsl_entity) {
        this.ejsl_entity = ejsl_entity;
    }
    public List<eJSL_Attribute> getEjsl_attributes() {
        return ejsl_attributes;
    }

    public void addEjsl_attribute(Ejsl_attribute ejsl_attribute) {
        this.ejsl_attributes.add(ejsl_attribute);
    }

}