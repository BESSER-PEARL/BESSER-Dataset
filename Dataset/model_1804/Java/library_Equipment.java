





import java.util.List;
import java.util.ArrayList;

public class library_Equipment extends Component {

    private String redundancy;
    private String state;
    private String equipmentCode;
    private String count;
    private String position;





    private library_NodeType library_nodetype;




    private library_ProductInfo library_productinfo;




    private library_Equipment library_equipment;




    private library_EquipmentGroup library_equipmentgroup;




    private List<library_EquipmentGroup> library_equipmentgroups;




    private List<library_Equipment> library_equipments;




    private List<library_EquipmentRelationship> library_equipmentrelationships;




    private library_EquipmentGroup library_equipmentgroup;


    public library_Equipment(
        String redundancy,        String state,        String equipmentCode,        String count,        String position    ) {
        super(
        );
        this.redundancy = redundancy;
        this.state = state;
        this.equipmentCode = equipmentCode;
        this.count = count;
        this.position = position;
        this.library_equipmentgroups = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
        this.library_equipmentrelationships = new ArrayList<>();
    }

    public library_Equipment(
        String redundancy,        String state,        String equipmentCode,        String count,        String position        ArrayList<library_EquipmentGroup> library_equipmentgroups,        ArrayList<library_Equipment> library_equipments,        ArrayList<library_EquipmentRelationship> library_equipmentrelationships    ) {
        this.redundancy = redundancy;
        this.state = state;
        this.equipmentCode = equipmentCode;
        this.count = count;
        this.position = position;
        this.library_equipmentgroups = library_equipmentgroups;
        this.library_equipments = library_equipments;
        this.library_equipmentrelationships = library_equipmentrelationships;
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

    public library_NodeType getLibrary_nodetype() {
        return library_nodetype;
    }

    public void setLibrary_nodetype(library_NodeType library_nodetype) {
        this.library_nodetype = library_nodetype;
    }
    public library_ProductInfo getLibrary_productinfo() {
        return library_productinfo;
    }

    public void setLibrary_productinfo(library_ProductInfo library_productinfo) {
        this.library_productinfo = library_productinfo;
    }
    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }
    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }
    public List<library_EquipmentGroup> getLibrary_equipmentgroups() {
        return library_equipmentgroups;
    }

    public void addLibrary_equipmentgroup(Library_equipmentgroup library_equipmentgroup) {
        this.library_equipmentgroups.add(library_equipmentgroup);
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public List<library_EquipmentRelationship> getLibrary_equipmentrelationships() {
        return library_equipmentrelationships;
    }

    public void addLibrary_equipmentrelationship(Library_equipmentrelationship library_equipmentrelationship) {
        this.library_equipmentrelationships.add(library_equipmentrelationship);
    }
    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }

}