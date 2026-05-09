





import java.util.List;
import java.util.ArrayList;

public class library_Parameter  {

    private String description;
    private String modifiable;
    private String expressionName;
    private String value;
    private String name;





    private library_EquipmentGroup library_equipmentgroup;




    private library_Equipment library_equipment;


    public library_Parameter(
        String description,        String modifiable,        String expressionName,        String value,        String name    ) {
        this.description = description;
        this.modifiable = modifiable;
        this.expressionName = expressionName;
        this.value = value;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getModifiable() {
        return modifiable;
    }

    public void setModifiable(String modifiable) {
        this.modifiable = modifiable;
    }
    public String getExpressionname() {
        return expressionName;
    }

    public void setExpressionname(String expressionName) {
        this.expressionName = expressionName;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }
    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }

}