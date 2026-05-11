





import java.util.List;
import java.util.ArrayList;

public class eJSL_Entitypackage  {

    private String name;





    private eJSL_Feature ejsl_feature;




    private List<eJSL_Datatype> ejsl_datatypes;




    private eJSL_Entitypackage ejsl_entitypackage;


    public eJSL_Entitypackage(
        String name    ) {
        this.name = name;
        this.ejsl_datatypes = new ArrayList<>();
    }

    public eJSL_Entitypackage(
        String name        ArrayList<eJSL_Datatype> ejsl_datatypes    ) {
        this.name = name;
        this.ejsl_datatypes = ejsl_datatypes;
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
    public List<eJSL_Datatype> getEjsl_datatypes() {
        return ejsl_datatypes;
    }

    public void addEjsl_datatype(Ejsl_datatype ejsl_datatype) {
        this.ejsl_datatypes.add(ejsl_datatype);
    }
    public eJSL_Entitypackage getEjsl_entitypackage() {
        return ejsl_entitypackage;
    }

    public void setEjsl_entitypackage(eJSL_Entitypackage ejsl_entitypackage) {
        this.ejsl_entitypackage = ejsl_entitypackage;
    }

}