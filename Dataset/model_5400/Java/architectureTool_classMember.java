





import java.util.List;
import java.util.ArrayList;

public class architectureTool_classMember  {

    private String name;





    private List<architectureTool_Method> architecturetool_methods;




    private List<architectureTool_Attribute> architecturetool_attributes;


    public architectureTool_classMember(
        String name    ) {
        this.name = name;
        this.architecturetool_methods = new ArrayList<>();
        this.architecturetool_attributes = new ArrayList<>();
    }

    public architectureTool_classMember(
        String name        ArrayList<architectureTool_Method> architecturetool_methods,        ArrayList<architectureTool_Attribute> architecturetool_attributes    ) {
        this.name = name;
        this.architecturetool_methods = architecturetool_methods;
        this.architecturetool_attributes = architecturetool_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<architectureTool_Method> getArchitecturetool_methods() {
        return architecturetool_methods;
    }

    public void addArchitecturetool_method(Architecturetool_method architecturetool_method) {
        this.architecturetool_methods.add(architecturetool_method);
    }
    public List<architectureTool_Attribute> getArchitecturetool_attributes() {
        return architecturetool_attributes;
    }

    public void addArchitecturetool_attribute(Architecturetool_attribute architecturetool_attribute) {
        this.architecturetool_attributes.add(architecturetool_attribute);
    }

}