





import java.util.List;
import java.util.ArrayList;

public class UseCase_UseCaseContainer  {






    private List<NamedElement> namedelements;


    public UseCase_UseCaseContainer(
    ) {
        this.namedelements = new ArrayList<>();
    }

    public UseCase_UseCaseContainer(
        ArrayList<NamedElement> namedelements    ) {
        this.namedelements = namedelements;
    }


    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }

}