





import java.util.List;
import java.util.ArrayList;

public class error4_Thing extends NamedElement {

    private int id;





    private error4_World error4_world;




    private List<error4_Component> error4_components;


    public error4_Thing(
        int id    ) {
        super(
        );
        this.id = id;
        this.error4_components = new ArrayList<>();
    }

    public error4_Thing(
        int id        ArrayList<error4_Component> error4_components    ) {
        this.id = id;
        this.error4_components = error4_components;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public error4_World getError4_world() {
        return error4_world;
    }

    public void setError4_world(error4_World error4_world) {
        this.error4_world = error4_world;
    }
    public List<error4_Component> getError4_components() {
        return error4_components;
    }

    public void addError4_component(Error4_component error4_component) {
        this.error4_components.add(error4_component);
    }

}