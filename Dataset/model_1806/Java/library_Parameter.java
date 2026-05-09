





import java.util.List;
import java.util.ArrayList;

public class library_Parameter extends Base {

    private String name;
    private String modifiable;
    private String value;
    private String description;
    private String expressionName;





    private library_EquipmentGroup library_equipmentgroup;




    private library_Component library_component;


    public library_Parameter(
        String name,        String modifiable,        String value,        String description,        String expressionName    ) {
        super(
        );
        this.name = name;
        this.modifiable = modifiable;
        this.value = value;
        this.description = description;
        this.expressionName = expressionName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getModifiable() {
        return modifiable;
    }

    public void setModifiable(String modifiable) {
        this.modifiable = modifiable;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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

    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }
    public library_Component getLibrary_component() {
        return library_component;
    }

    public void setLibrary_component(library_Component library_component) {
        this.library_component = library_component;
    }

}