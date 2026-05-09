





import java.util.List;
import java.util.ArrayList;

public class dsl_Eclass  {

    private String name;





    private dsl_MethodBack dsl_methodback;




    private dsl_AbstractMethod dsl_abstractmethod;




    private dsl_Attribute dsl_attribute;




    private dsl_AbstractMethod dsl_abstractmethod;




    private dsl_Epackage dsl_epackage;




    private dsl_MethodBack dsl_methodback;


    public dsl_Eclass(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_MethodBack getDsl_methodback() {
        return dsl_methodback;
    }

    public void setDsl_methodback(dsl_MethodBack dsl_methodback) {
        this.dsl_methodback = dsl_methodback;
    }
    public dsl_AbstractMethod getDsl_abstractmethod() {
        return dsl_abstractmethod;
    }

    public void setDsl_abstractmethod(dsl_AbstractMethod dsl_abstractmethod) {
        this.dsl_abstractmethod = dsl_abstractmethod;
    }
    public dsl_Attribute getDsl_attribute() {
        return dsl_attribute;
    }

    public void setDsl_attribute(dsl_Attribute dsl_attribute) {
        this.dsl_attribute = dsl_attribute;
    }
    public dsl_AbstractMethod getDsl_abstractmethod() {
        return dsl_abstractmethod;
    }

    public void setDsl_abstractmethod(dsl_AbstractMethod dsl_abstractmethod) {
        this.dsl_abstractmethod = dsl_abstractmethod;
    }
    public dsl_Epackage getDsl_epackage() {
        return dsl_epackage;
    }

    public void setDsl_epackage(dsl_Epackage dsl_epackage) {
        this.dsl_epackage = dsl_epackage;
    }
    public dsl_MethodBack getDsl_methodback() {
        return dsl_methodback;
    }

    public void setDsl_methodback(dsl_MethodBack dsl_methodback) {
        this.dsl_methodback = dsl_methodback;
    }

}