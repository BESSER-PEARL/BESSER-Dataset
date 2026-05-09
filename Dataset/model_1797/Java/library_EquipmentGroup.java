





import java.util.List;
import java.util.ArrayList;

public class library_EquipmentGroup  {

    private String description;
    private String name;
    private String count;





    private List<library_Equipment> library_equipments;




    private library_Equipment library_equipment;




    private List<library_Expression> library_expressions;




    private List<library_Equipment> library_equipments;




    private library_Expression library_expression;




    private List<library_DiagramInfo> library_diagraminfos;


    public library_EquipmentGroup(
        String description,        String name,        String count    ) {
        this.description = description;
        this.name = name;
        this.count = count;
        this.library_equipments = new ArrayList<>();
        this.library_expressions = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
        this.library_diagraminfos = new ArrayList<>();
    }

    public library_EquipmentGroup(
        String description,        String name,        String count        ArrayList<library_Equipment> library_equipments,        ArrayList<library_Expression> library_expressions,        ArrayList<library_Equipment> library_equipments,        ArrayList<library_DiagramInfo> library_diagraminfos    ) {
        this.description = description;
        this.name = name;
        this.count = count;
        this.library_equipments = library_equipments;
        this.library_expressions = library_expressions;
        this.library_equipments = library_equipments;
        this.library_diagraminfos = library_diagraminfos;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }
    public List<library_Expression> getLibrary_expressions() {
        return library_expressions;
    }

    public void addLibrary_expression(Library_expression library_expression) {
        this.library_expressions.add(library_expression);
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public library_Expression getLibrary_expression() {
        return library_expression;
    }

    public void setLibrary_expression(library_Expression library_expression) {
        this.library_expression = library_expression;
    }
    public List<library_DiagramInfo> getLibrary_diagraminfos() {
        return library_diagraminfos;
    }

    public void addLibrary_diagraminfo(Library_diagraminfo library_diagraminfo) {
        this.library_diagraminfos.add(library_diagraminfo);
    }

}