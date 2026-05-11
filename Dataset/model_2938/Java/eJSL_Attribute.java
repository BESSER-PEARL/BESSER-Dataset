





import java.util.List;
import java.util.ArrayList;

public class eJSL_Attribute  {

    private boolean preserve;
    private String name;
    private boolean id;
    private boolean isunique;
    private boolean isprimary;





    private eJSL_Attribute ejsl_attribute;




    private eJSL_Entity ejsl_entity;




    private eJSL_Type ejsl_type;




    private eJSL_DynamicPage ejsl_dynamicpage;




    private eJSL_DynamicPage ejsl_dynamicpage;




    private eJSL_Link ejsl_link;


    public eJSL_Attribute(
        boolean preserve,        String name,        boolean id,        boolean isunique,        boolean isprimary    ) {
        this.preserve = preserve;
        this.name = name;
        this.id = id;
        this.isunique = isunique;
        this.isprimary = isprimary;
    }


    public boolean getPreserve() {
        return preserve;
    }

    public void setPreserve(boolean preserve) {
        this.preserve = preserve;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getId() {
        return id;
    }

    public void setId(boolean id) {
        this.id = id;
    }
    public boolean getIsunique() {
        return isunique;
    }

    public void setIsunique(boolean isunique) {
        this.isunique = isunique;
    }
    public boolean getIsprimary() {
        return isprimary;
    }

    public void setIsprimary(boolean isprimary) {
        this.isprimary = isprimary;
    }

    public eJSL_Attribute getEjsl_attribute() {
        return ejsl_attribute;
    }

    public void setEjsl_attribute(eJSL_Attribute ejsl_attribute) {
        this.ejsl_attribute = ejsl_attribute;
    }
    public eJSL_Entity getEjsl_entity() {
        return ejsl_entity;
    }

    public void setEjsl_entity(eJSL_Entity ejsl_entity) {
        this.ejsl_entity = ejsl_entity;
    }
    public eJSL_Type getEjsl_type() {
        return ejsl_type;
    }

    public void setEjsl_type(eJSL_Type ejsl_type) {
        this.ejsl_type = ejsl_type;
    }
    public eJSL_DynamicPage getEjsl_dynamicpage() {
        return ejsl_dynamicpage;
    }

    public void setEjsl_dynamicpage(eJSL_DynamicPage ejsl_dynamicpage) {
        this.ejsl_dynamicpage = ejsl_dynamicpage;
    }
    public eJSL_DynamicPage getEjsl_dynamicpage() {
        return ejsl_dynamicpage;
    }

    public void setEjsl_dynamicpage(eJSL_DynamicPage ejsl_dynamicpage) {
        this.ejsl_dynamicpage = ejsl_dynamicpage;
    }
    public eJSL_Link getEjsl_link() {
        return ejsl_link;
    }

    public void setEjsl_link(eJSL_Link ejsl_link) {
        this.ejsl_link = ejsl_link;
    }

}