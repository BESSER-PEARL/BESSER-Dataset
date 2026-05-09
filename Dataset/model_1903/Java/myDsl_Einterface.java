





import java.util.List;
import java.util.ArrayList;

public class myDsl_Einterface  {

    private String name;





    private myDsl_GenericClass mydsl_genericclass;




    private List<myDsl_AbstractMethod> mydsl_abstractmethods;




    private List<myDsl_Attribute> mydsl_attributes;


    public myDsl_Einterface(
        String name    ) {
        this.name = name;
        this.mydsl_abstractmethods = new ArrayList<>();
        this.mydsl_attributes = new ArrayList<>();
    }

    public myDsl_Einterface(
        String name        ArrayList<myDsl_AbstractMethod> mydsl_abstractmethods,        ArrayList<myDsl_Attribute> mydsl_attributes    ) {
        this.name = name;
        this.mydsl_abstractmethods = mydsl_abstractmethods;
        this.mydsl_attributes = mydsl_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_GenericClass getMydsl_genericclass() {
        return mydsl_genericclass;
    }

    public void setMydsl_genericclass(myDsl_GenericClass mydsl_genericclass) {
        this.mydsl_genericclass = mydsl_genericclass;
    }
    public List<myDsl_AbstractMethod> getMydsl_abstractmethods() {
        return mydsl_abstractmethods;
    }

    public void addMydsl_abstractmethod(Mydsl_abstractmethod mydsl_abstractmethod) {
        this.mydsl_abstractmethods.add(mydsl_abstractmethod);
    }
    public List<myDsl_Attribute> getMydsl_attributes() {
        return mydsl_attributes;
    }

    public void addMydsl_attribute(Mydsl_attribute mydsl_attribute) {
        this.mydsl_attributes.add(mydsl_attribute);
    }

}