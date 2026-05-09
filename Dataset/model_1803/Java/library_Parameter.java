





import java.util.List;
import java.util.ArrayList;

public class library_Parameter extends Base {

    private String description;
    private String expressionName;
    private String name;
    private String value;
    private String modifiable;





    private library_Component library_component;




    private library_EquipmentGroup library_equipmentgroup;


    public library_Parameter(
        String description,        String expressionName,        String name,        String value,        String modifiable    ) {
        super(
        );
        this.description = description;
        this.expressionName = expressionName;
        this.name = name;
        this.value = value;
        this.modifiable = modifiable;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getExpressionname() {
        return expressionName;
    }

    public void setExpressionname(String expressionName) {
        this.expressionName = expressionName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getModifiable() {
        return modifiable;
    }

    public void setModifiable(String modifiable) {
        this.modifiable = modifiable;
    }

    public library_Component getLibrary_component() {
        return library_component;
    }

    public void setLibrary_component(library_Component library_component) {
        this.library_component = library_component;
    }
    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }

}