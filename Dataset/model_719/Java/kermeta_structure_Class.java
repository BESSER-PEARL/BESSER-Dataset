





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Class extends ParameterizedType {

    private String isAbstract;
    private String name;





    private List<structure_Operation> structure_operations;




    private List<structure_Property> structure_propertys;


    public kermeta_structure_Class(
        String isAbstract,        String name    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.name = name;
        this.structure_operations = new ArrayList<>();
        this.structure_propertys = new ArrayList<>();
    }

    public kermeta_structure_Class(
        String isAbstract,        String name        ArrayList<structure_Operation> structure_operations,        ArrayList<structure_Property> structure_propertys    ) {
        this.isAbstract = isAbstract;
        this.name = name;
        this.structure_operations = structure_operations;
        this.structure_propertys = structure_propertys;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<structure_Operation> getStructure_operations() {
        return structure_operations;
    }

    public void addStructure_operation(Structure_operation structure_operation) {
        this.structure_operations.add(structure_operation);
    }
    public List<structure_Property> getStructure_propertys() {
        return structure_propertys;
    }

    public void addStructure_property(Structure_property structure_property) {
        this.structure_propertys.add(structure_property);
    }

}