





import java.util.List;
import java.util.ArrayList;

public class library_Expression  {

    private String name;
    private String expressionLines;





    private library_Equipment library_equipment;




    private List<library_Equipment> library_equipments;


    public library_Expression(
        String name,        String expressionLines    ) {
        this.name = name;
        this.expressionLines = expressionLines;
        this.library_equipments = new ArrayList<>();
    }

    public library_Expression(
        String name,        String expressionLines        ArrayList<library_Equipment> library_equipments    ) {
        this.name = name;
        this.expressionLines = expressionLines;
        this.library_equipments = library_equipments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExpressionlines() {
        return expressionLines;
    }

    public void setExpressionlines(String expressionLines) {
        this.expressionLines = expressionLines;
    }

    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }

}