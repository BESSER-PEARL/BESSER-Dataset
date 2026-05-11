





import java.util.List;
import java.util.ArrayList;

public class eJSL_Class  {

    private String name;





    private List<eJSL_Entity> ejsl_entitys;




    private eJSL_Class ejsl_class;




    private eJSL_Library ejsl_library;




    private List<eJSL_Class> ejsl_classs;


    public eJSL_Class(
        String name    ) {
        this.name = name;
        this.ejsl_entitys = new ArrayList<>();
        this.ejsl_classs = new ArrayList<>();
    }

    public eJSL_Class(
        String name        ArrayList<eJSL_Entity> ejsl_entitys,        ArrayList<eJSL_Class> ejsl_classs    ) {
        this.name = name;
        this.ejsl_entitys = ejsl_entitys;
        this.ejsl_classs = ejsl_classs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eJSL_Entity> getEjsl_entitys() {
        return ejsl_entitys;
    }

    public void addEjsl_entity(Ejsl_entity ejsl_entity) {
        this.ejsl_entitys.add(ejsl_entity);
    }
    public eJSL_Class getEjsl_class() {
        return ejsl_class;
    }

    public void setEjsl_class(eJSL_Class ejsl_class) {
        this.ejsl_class = ejsl_class;
    }
    public eJSL_Library getEjsl_library() {
        return ejsl_library;
    }

    public void setEjsl_library(eJSL_Library ejsl_library) {
        this.ejsl_library = ejsl_library;
    }
    public List<eJSL_Class> getEjsl_classs() {
        return ejsl_classs;
    }

    public void addEjsl_class(Ejsl_class ejsl_class) {
        this.ejsl_classs.add(ejsl_class);
    }

}