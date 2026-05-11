





import java.util.List;
import java.util.ArrayList;

public class thingml_AnnotatedElement extends ThingMLElement {






    private List<thingml_PlatformAnnotation> thingml_platformannotations;


    public thingml_AnnotatedElement(
    ) {
        super(
        );
        this.thingml_platformannotations = new ArrayList<>();
    }

    public thingml_AnnotatedElement(
        ArrayList<thingml_PlatformAnnotation> thingml_platformannotations    ) {
        this.thingml_platformannotations = thingml_platformannotations;
    }


    public List<thingml_PlatformAnnotation> getThingml_platformannotations() {
        return thingml_platformannotations;
    }

    public void addThingml_platformannotation(Thingml_platformannotation thingml_platformannotation) {
        this.thingml_platformannotations.add(thingml_platformannotation);
    }

}