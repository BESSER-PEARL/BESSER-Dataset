





import java.util.List;
import java.util.ArrayList;

public class eJSL_Entity  {

    private boolean preserve;
    private String name;





    private eJSL_Feature ejsl_feature;




    private eJSL_Entity ejsl_entity;




    private eJSL_Entitypackage ejsl_entitypackage;


    public eJSL_Entity(
        boolean preserve,        String name    ) {
        this.preserve = preserve;
        this.name = name;
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

    public eJSL_Feature getEjsl_feature() {
        return ejsl_feature;
    }

    public void setEjsl_feature(eJSL_Feature ejsl_feature) {
        this.ejsl_feature = ejsl_feature;
    }
    public eJSL_Entity getEjsl_entity() {
        return ejsl_entity;
    }

    public void setEjsl_entity(eJSL_Entity ejsl_entity) {
        this.ejsl_entity = ejsl_entity;
    }
    public eJSL_Entitypackage getEjsl_entitypackage() {
        return ejsl_entitypackage;
    }

    public void setEjsl_entitypackage(eJSL_Entitypackage ejsl_entitypackage) {
        this.ejsl_entitypackage = ejsl_entitypackage;
    }

}