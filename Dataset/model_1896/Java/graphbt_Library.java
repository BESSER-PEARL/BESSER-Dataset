





import java.util.List;
import java.util.ArrayList;

public class graphbt_Library  {

    private String location;
    private String name;
    private String text;
    private String id;
    private String desc;





    private graphbt_Component graphbt_component;




    private List<graphbt_MethodDeclaration> graphbt_methoddeclarations;




    private List<graphbt_Attribute> graphbt_attributes;




    private List<graphbt_State> graphbt_states;




    private List<graphbt_Behavior> graphbt_behaviors;


    public graphbt_Library(
        String location,        String name,        String text,        String id,        String desc    ) {
        this.location = location;
        this.name = name;
        this.text = text;
        this.id = id;
        this.desc = desc;
        this.graphbt_methoddeclarations = new ArrayList<>();
        this.graphbt_attributes = new ArrayList<>();
        this.graphbt_states = new ArrayList<>();
        this.graphbt_behaviors = new ArrayList<>();
    }

    public graphbt_Library(
        String location,        String name,        String text,        String id,        String desc        ArrayList<graphbt_MethodDeclaration> graphbt_methoddeclarations,        ArrayList<graphbt_Attribute> graphbt_attributes,        ArrayList<graphbt_State> graphbt_states,        ArrayList<graphbt_Behavior> graphbt_behaviors    ) {
        this.location = location;
        this.name = name;
        this.text = text;
        this.id = id;
        this.desc = desc;
        this.graphbt_methoddeclarations = graphbt_methoddeclarations;
        this.graphbt_attributes = graphbt_attributes;
        this.graphbt_states = graphbt_states;
        this.graphbt_behaviors = graphbt_behaviors;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }
    public List<graphbt_MethodDeclaration> getGraphbt_methoddeclarations() {
        return graphbt_methoddeclarations;
    }

    public void addGraphbt_methoddeclaration(Graphbt_methoddeclaration graphbt_methoddeclaration) {
        this.graphbt_methoddeclarations.add(graphbt_methoddeclaration);
    }
    public List<graphbt_Attribute> getGraphbt_attributes() {
        return graphbt_attributes;
    }

    public void addGraphbt_attribute(Graphbt_attribute graphbt_attribute) {
        this.graphbt_attributes.add(graphbt_attribute);
    }
    public List<graphbt_State> getGraphbt_states() {
        return graphbt_states;
    }

    public void addGraphbt_state(Graphbt_state graphbt_state) {
        this.graphbt_states.add(graphbt_state);
    }
    public List<graphbt_Behavior> getGraphbt_behaviors() {
        return graphbt_behaviors;
    }

    public void addGraphbt_behavior(Graphbt_behavior graphbt_behavior) {
        this.graphbt_behaviors.add(graphbt_behavior);
    }

}