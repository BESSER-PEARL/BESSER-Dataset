





import java.util.List;
import java.util.ArrayList;

public class component_ConfigurationSet extends WrapperObject {

    private String id;





    private List<component_NameValue> component_namevalues;




    private component_Component component_component;




    private component_Component component_component;


    public component_ConfigurationSet(
        String id    ) {
        super(
        );
        this.id = id;
        this.component_namevalues = new ArrayList<>();
    }

    public component_ConfigurationSet(
        String id        ArrayList<component_NameValue> component_namevalues    ) {
        this.id = id;
        this.component_namevalues = component_namevalues;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<component_NameValue> getComponent_namevalues() {
        return component_namevalues;
    }

    public void addComponent_namevalue(Component_namevalue component_namevalue) {
        this.component_namevalues.add(component_namevalue);
    }
    public component_Component getComponent_component() {
        return component_component;
    }

    public void setComponent_component(component_Component component_component) {
        this.component_component = component_component;
    }
    public component_Component getComponent_component() {
        return component_component;
    }

    public void setComponent_component(component_Component component_component) {
        this.component_component = component_component;
    }

}