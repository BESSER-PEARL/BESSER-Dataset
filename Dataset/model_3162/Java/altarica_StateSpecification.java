





import java.util.List;
import java.util.ArrayList;

public class altarica_StateSpecification extends AbstractSpecification {






    private List<altarica_StateDeclaration> altarica_statedeclarations;


    public altarica_StateSpecification(
    ) {
        super(
        );
        this.altarica_statedeclarations = new ArrayList<>();
    }

    public altarica_StateSpecification(
        ArrayList<altarica_StateDeclaration> altarica_statedeclarations    ) {
        this.altarica_statedeclarations = altarica_statedeclarations;
    }


    public List<altarica_StateDeclaration> getAltarica_statedeclarations() {
        return altarica_statedeclarations;
    }

    public void addAltarica_statedeclaration(Altarica_statedeclaration altarica_statedeclaration) {
        this.altarica_statedeclarations.add(altarica_statedeclaration);
    }

}