





import java.util.List;
import java.util.ArrayList;

public class Classes_Dependencies_Dependency extends Kernel_PackageableElement, Kernel_DirectedRelationship {






    private List<NamedElement> namedelements;




    private List<NamedElement> namedelements;


    public Classes_Dependencies_Dependency(
    ) {
        super(
        );
        this.namedelements = new ArrayList<>();
        this.namedelements = new ArrayList<>();
    }

    public Classes_Dependencies_Dependency(
        ArrayList<NamedElement> namedelements,        ArrayList<NamedElement> namedelements    ) {
        this.namedelements = namedelements;
        this.namedelements = namedelements;
    }


    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }
    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }

}