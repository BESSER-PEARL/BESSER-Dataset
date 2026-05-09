





import java.util.List;
import java.util.ArrayList;

public class library_Expression  {

    private String expressionLines;
    private String name;





    private List<library_Equipment> library_equipments;




    private library_Equipment library_equipment;




    private library_Equipment library_equipment;


    public library_Expression(
        String expressionLines,        String name    ) {
        this.expressionLines = expressionLines;
        this.name = name;
        this.library_equipments = new ArrayList<>();
    }

    public library_Expression(
        String expressionLines,        String name        ArrayList<library_Equipment> library_equipments    ) {
        this.expressionLines = expressionLines;
        this.name = name;
        this.library_equipments = library_equipments;
    }

    public String getExpressionlines() {
        return expressionLines;
    }

    public void setExpressionlines(String expressionLines) {
        this.expressionLines = expressionLines;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }

}