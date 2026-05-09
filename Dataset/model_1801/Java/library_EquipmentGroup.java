





import java.util.List;
import java.util.ArrayList;

public class library_EquipmentGroup extends Base {

    private String name;
    private String count;
    private String description;





    private List<library_Equipment> library_equipments;




    private List<library_Equipment> library_equipments;




    private List<library_Parameter> library_parameters;




    private library_Equipment library_equipment;


    public library_EquipmentGroup(
        String name,        String count,        String description    ) {
        super(
        );
        this.name = name;
        this.count = count;
        this.description = description;
        this.library_equipments = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
        this.library_parameters = new ArrayList<>();
    }

    public library_EquipmentGroup(
        String name,        String count,        String description        ArrayList<library_Equipment> library_equipments,        ArrayList<library_Equipment> library_equipments,        ArrayList<library_Parameter> library_parameters    ) {
        this.name = name;
        this.count = count;
        this.description = description;
        this.library_equipments = library_equipments;
        this.library_equipments = library_equipments;
        this.library_parameters = library_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public List<library_Parameter> getLibrary_parameters() {
        return library_parameters;
    }

    public void addLibrary_parameter(Library_parameter library_parameter) {
        this.library_parameters.add(library_parameter);
    }
    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }

}