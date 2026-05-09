





import java.util.List;
import java.util.ArrayList;

public class library_Expression extends Base {

    private String name;
    private String expressionLines;





    private library_EquipmentGroup library_equipmentgroup;




    private library_Component library_component;




    private library_Tolerance library_tolerance;




    private library_Component library_component;


    public library_Expression(
        String name,        String expressionLines    ) {
        super(
        );
        this.name = name;
        this.expressionLines = expressionLines;
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
    public library_Tolerance getLibrary_tolerance() {
        return library_tolerance;
    }

    public void setLibrary_tolerance(library_Tolerance library_tolerance) {
        this.library_tolerance = library_tolerance;
    }
    public library_Component getLibrary_component() {
        return library_component;
    }

    public void setLibrary_component(library_Component library_component) {
        this.library_component = library_component;
    }

}