





import java.util.List;
import java.util.ArrayList;

public class thingML_EnumerationLiteral  {

    private String name;





    private thingML_Enumeration thingml_enumeration;




    private List<thingML_PlatformAnnotation> thingml_platformannotations;


    public thingML_EnumerationLiteral(
        String name    ) {
        this.name = name;
        this.thingml_platformannotations = new ArrayList<>();
    }

    public thingML_EnumerationLiteral(
        String name        ArrayList<thingML_PlatformAnnotation> thingml_platformannotations    ) {
        this.name = name;
        this.thingml_platformannotations = thingml_platformannotations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public thingML_Enumeration getThingml_enumeration() {
        return thingml_enumeration;
    }

    public void setThingml_enumeration(thingML_Enumeration thingml_enumeration) {
        this.thingml_enumeration = thingml_enumeration;
    }
    public List<thingML_PlatformAnnotation> getThingml_platformannotations() {
        return thingml_platformannotations;
    }

    public void addThingml_platformannotation(Thingml_platformannotation thingml_platformannotation) {
        this.thingml_platformannotations.add(thingml_platformannotation);
    }

}