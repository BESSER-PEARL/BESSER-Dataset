





import java.util.List;
import java.util.ArrayList;

public class thingML_AnnotatedElement  {






    private List<thingML_PlatformAnnotation> thingml_platformannotations;


    public thingML_AnnotatedElement(
    ) {
        this.thingml_platformannotations = new ArrayList<>();
    }

    public thingML_AnnotatedElement(
        ArrayList<thingML_PlatformAnnotation> thingml_platformannotations    ) {
        this.thingml_platformannotations = thingml_platformannotations;
    }


    public List<thingML_PlatformAnnotation> getThingml_platformannotations() {
        return thingml_platformannotations;
    }

    public void addThingml_platformannotation(Thingml_platformannotation thingml_platformannotation) {
        this.thingml_platformannotations.add(thingml_platformannotation);
    }

}