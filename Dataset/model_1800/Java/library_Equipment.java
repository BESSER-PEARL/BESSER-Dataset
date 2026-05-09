





import java.util.List;
import java.util.ArrayList;

public class library_Equipment  {

    private String description;
    private String count;
    private String position;
    private String redundancy;
    private String state;
    private String equipmentCode;
    private String equipmentName;





    private List<library_Equipment> library_equipments;




    private List<library_Equipment> library_equipments;


    public library_Equipment(
        String description,        String count,        String position,        String redundancy,        String state,        String equipmentCode,        String equipmentName    ) {
        this.description = description;
        this.count = count;
        this.position = position;
        this.redundancy = redundancy;
        this.state = state;
        this.equipmentCode = equipmentCode;
        this.equipmentName = equipmentName;
        this.library_equipments = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
    }

    public library_Equipment(
        String description,        String count,        String position,        String redundancy,        String state,        String equipmentCode,        String equipmentName        ArrayList<library_Equipment> library_equipments,        ArrayList<library_Equipment> library_equipments    ) {
        this.description = description;
        this.count = count;
        this.position = position;
        this.redundancy = redundancy;
        this.state = state;
        this.equipmentCode = equipmentCode;
        this.equipmentName = equipmentName;
        this.library_equipments = library_equipments;
        this.library_equipments = library_equipments;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getRedundancy() {
        return redundancy;
    }

    public void setRedundancy(String redundancy) {
        this.redundancy = redundancy;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getEquipmentcode() {
        return equipmentCode;
    }

    public void setEquipmentcode(String equipmentCode) {
        this.equipmentCode = equipmentCode;
    }
    public String getEquipmentname() {
        return equipmentName;
    }

    public void setEquipmentname(String equipmentName) {
        this.equipmentName = equipmentName;
    }

    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }

}