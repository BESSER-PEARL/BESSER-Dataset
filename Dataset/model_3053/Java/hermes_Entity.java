





import java.util.List;
import java.util.ArrayList;

public class hermes_Entity extends NamedElement {

    private String annotations;





    private hermes_Package hermes_package;




    private hermes_Entity hermes_entity;


    public hermes_Entity(
        String annotations    ) {
        super(
        );
        this.annotations = annotations;
    }


    public String getAnnotations() {
        return annotations;
    }

    public void setAnnotations(String annotations) {
        this.annotations = annotations;
    }

    public hermes_Package getHermes_package() {
        return hermes_package;
    }

    public void setHermes_package(hermes_Package hermes_package) {
        this.hermes_package = hermes_package;
    }
    public hermes_Entity getHermes_entity() {
        return hermes_entity;
    }

    public void setHermes_entity(hermes_Entity hermes_entity) {
        this.hermes_entity = hermes_entity;
    }

}