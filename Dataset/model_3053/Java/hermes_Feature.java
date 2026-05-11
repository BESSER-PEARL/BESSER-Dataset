





import java.util.List;
import java.util.ArrayList;

public class hermes_Feature extends NamedElement {

    private String annotations;
    private boolean many;





    private hermes_Entity hermes_entity;


    public hermes_Feature(
        String annotations,        boolean many    ) {
        super(
        );
        this.annotations = annotations;
        this.many = many;
    }


    public String getAnnotations() {
        return annotations;
    }

    public void setAnnotations(String annotations) {
        this.annotations = annotations;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public hermes_Entity getHermes_entity() {
        return hermes_entity;
    }

    public void setHermes_entity(hermes_Entity hermes_entity) {
        this.hermes_entity = hermes_entity;
    }

}