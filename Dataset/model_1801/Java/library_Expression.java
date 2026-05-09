





import java.util.List;
import java.util.ArrayList;

public class library_Expression extends Base {

    private String expressionLines;
    private String name;





    private library_EquipmentGroup library_equipmentgroup;




    private library_EObject library_eobject;




    private library_Component library_component;




    private library_Component library_component;




    private library_Tolerance library_tolerance;




    private library_Library library_library;


    public library_Expression(
        String expressionLines,        String name    ) {
        super(
        );
        this.expressionLines = expressionLines;
        this.name = name;
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

    public library_EquipmentGroup getLibrary_equipmentgroup() {
        return library_equipmentgroup;
    }

    public void setLibrary_equipmentgroup(library_EquipmentGroup library_equipmentgroup) {
        this.library_equipmentgroup = library_equipmentgroup;
    }
    public library_EObject getLibrary_eobject() {
        return library_eobject;
    }

    public void setLibrary_eobject(library_EObject library_eobject) {
        this.library_eobject = library_eobject;
    }
    public library_Component getLibrary_component() {
        return library_component;
    }

    public void setLibrary_component(library_Component library_component) {
        this.library_component = library_component;
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
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}