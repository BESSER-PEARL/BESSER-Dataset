





import java.util.List;
import java.util.ArrayList;

public class dsl_Einterface  {

    private String name;





    private dsl_GenericClass dsl_genericclass;




    private List<dsl_AbstractMethod> dsl_abstractmethods;




    private List<dsl_Attribute> dsl_attributes;


    public dsl_Einterface(
        String name    ) {
        this.name = name;
        this.dsl_abstractmethods = new ArrayList<>();
        this.dsl_attributes = new ArrayList<>();
    }

    public dsl_Einterface(
        String name        ArrayList<dsl_AbstractMethod> dsl_abstractmethods,        ArrayList<dsl_Attribute> dsl_attributes    ) {
        this.name = name;
        this.dsl_abstractmethods = dsl_abstractmethods;
        this.dsl_attributes = dsl_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_GenericClass getDsl_genericclass() {
        return dsl_genericclass;
    }

    public void setDsl_genericclass(dsl_GenericClass dsl_genericclass) {
        this.dsl_genericclass = dsl_genericclass;
    }
    public List<dsl_AbstractMethod> getDsl_abstractmethods() {
        return dsl_abstractmethods;
    }

    public void addDsl_abstractmethod(Dsl_abstractmethod dsl_abstractmethod) {
        this.dsl_abstractmethods.add(dsl_abstractmethod);
    }
    public List<dsl_Attribute> getDsl_attributes() {
        return dsl_attributes;
    }

    public void addDsl_attribute(Dsl_attribute dsl_attribute) {
        this.dsl_attributes.add(dsl_attribute);
    }

}