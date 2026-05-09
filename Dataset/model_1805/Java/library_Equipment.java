





import java.util.List;
import java.util.ArrayList;

public class library_Equipment extends Component {

    private String redundancy;
    private String count;
    private String state;
    private String position;
    private String equipmentCode;





    private library_EquipmentGroup library_equipmentgroup;




    private List<library_Equipment> library_equipments;




    private library_EquipmentGroup library_equipmentgroup;




    private List<library_EquipmentGroup> library_equipmentgroups;




    private List<library_Equipment> library_equipments;




    private library_ProductInfo library_productinfo;




    private library_NodeType library_nodetype;


    public library_Equipment(
        String redundancy,        String count,        String state,        String position,        String equipmentCode    ) {
        super(
        );
        this.redundancy = redundancy;
        this.count = count;
        this.state = state;
        this.position = position;
        this.equipmentCode = equipmentCode;
        this.library_equipments = new ArrayList<>();
        this.library_equipmentgroups = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
    }

    public library_Equipment(
        String redundancy,        String count,        String state,        String position,        String equipmentCode        ArrayList<library_Equipment> library_equipments,        ArrayList<library_EquipmentGroup> library_equipmentgroups,        ArrayList<library_Equipment> library_equipments    ) {
        this.redundancy = redundancy;
        this.count = count;
        this.state = state;
        this.position = position;
        this.equipmentCode = equipmentCode;
        this.library_equipments = library_equipments;
        this.library_equipmentgroups = library_equipmentgroups;
        this.library_equipments = library_equipments;
    }

    public String getRedundancy() {
        return redundancy;
    }

    public void setRedundancy(String redundancy) {
        this.redundancy = redundancy;
    }
    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getEquipmentcode() {
        return equipmentCode;
    }

    public void setEquipmentcode(String equipmentCode) {
        this.equipmentCode = equipmentCode;
    }

    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
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
    public library_ProductInfo getLibrary_productinfo() {
        return library_productinfo;
    }

    public void setLibrary_productinfo(library_ProductInfo library_productinfo) {
        this.library_productinfo = library_productinfo;
    }
    public library_NodeType getLibrary_nodetype() {
        return library_nodetype;
    }

    public void setLibrary_nodetype(library_NodeType library_nodetype) {
        this.library_nodetype = library_nodetype;
    }

}