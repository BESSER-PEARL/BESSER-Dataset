





import java.util.List;
import java.util.ArrayList;

public class td1_Program  {

    private int ComponentSize;
    private String Name;





    private List<td1_DataType> td1_datatypes;




    private List<td1_Component> td1_components;


    public td1_Program(
        int ComponentSize,        String Name    ) {
        this.ComponentSize = ComponentSize;
        this.Name = Name;
        this.td1_datatypes = new ArrayList<>();
        this.td1_components = new ArrayList<>();
    }

    public td1_Program(
        int ComponentSize,        String Name        ArrayList<td1_DataType> td1_datatypes,        ArrayList<td1_Component> td1_components    ) {
        this.ComponentSize = ComponentSize;
        this.Name = Name;
        this.td1_datatypes = td1_datatypes;
        this.td1_components = td1_components;
    }

    public int getComponentsize() {
        return ComponentSize;
    }

    public void setComponentsize(int ComponentSize) {
        this.ComponentSize = ComponentSize;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<td1_DataType> getTd1_datatypes() {
        return td1_datatypes;
    }

    public void addTd1_datatype(Td1_datatype td1_datatype) {
        this.td1_datatypes.add(td1_datatype);
    }
    public List<td1_Component> getTd1_components() {
        return td1_components;
    }

    public void addTd1_component(Td1_component td1_component) {
        this.td1_components.add(td1_component);
    }

}