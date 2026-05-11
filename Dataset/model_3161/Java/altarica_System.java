





import java.util.List;
import java.util.ArrayList;

public class altarica_System  {






    private List<altarica_AbstractDeclaration> altarica_abstractdeclarations;


    public altarica_System(
    ) {
        this.altarica_abstractdeclarations = new ArrayList<>();
    }

    public altarica_System(
        ArrayList<altarica_AbstractDeclaration> altarica_abstractdeclarations    ) {
        this.altarica_abstractdeclarations = altarica_abstractdeclarations;
    }


    public List<altarica_AbstractDeclaration> getAltarica_abstractdeclarations() {
        return altarica_abstractdeclarations;
    }

    public void addAltarica_abstractdeclaration(Altarica_abstractdeclaration altarica_abstractdeclaration) {
        this.altarica_abstractdeclarations.add(altarica_abstractdeclaration);
    }

}