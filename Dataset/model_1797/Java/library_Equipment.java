





import java.util.List;
import java.util.ArrayList;

public class library_Equipment  {

    private String count;
    private String redundancy;
    private String description;
    private String state;
    private String equipmentCode;
    private String equipmentName;
    private String position;





    private List<library_DiagramInfo> library_diagraminfos;




    private List<library_Equipment> library_equipments;




    private List<library_Equipment> library_equipments;


    public library_Equipment(
        String count,        String redundancy,        String description,        String state,        String equipmentCode,        String equipmentName,        String position    ) {
        this.count = count;
        this.redundancy = redundancy;
        this.description = description;
        this.state = state;
        this.equipmentCode = equipmentCode;
        this.equipmentName = equipmentName;
        this.position = position;
        this.library_diagraminfos = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
    }

    public library_Equipment(
        String count,        String redundancy,        String description,        String state,        String equipmentCode,        String equipmentName,        String position        ArrayList<library_DiagramInfo> library_diagraminfos,        ArrayList<library_Equipment> library_equipments,        ArrayList<library_Equipment> library_equipments    ) {
        this.count = count;
        this.redundancy = redundancy;
        this.description = description;
        this.state = state;
        this.equipmentCode = equipmentCode;
        this.equipmentName = equipmentName;
        this.position = position;
        this.library_diagraminfos = library_diagraminfos;
        this.library_equipments = library_equipments;
        this.library_equipments = library_equipments;
    }

    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }
    public String getRedundancy() {
        return redundancy;
    }

    public void setRedundancy(String redundancy) {
        this.redundancy = redundancy;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public List<library_DiagramInfo> getLibrary_diagraminfos() {
        return library_diagraminfos;
    }

    public void addLibrary_diagraminfo(Library_diagraminfo library_diagraminfo) {
        this.library_diagraminfos.add(library_diagraminfo);
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