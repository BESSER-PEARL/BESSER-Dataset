





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Component extends Classifier {






    private List<ElementResidence> elementresidences;


    public foundation_core_Component(
    ) {
        super(
        );
        this.elementresidences = new ArrayList<>();
    }

    public foundation_core_Component(
        ArrayList<ElementResidence> elementresidences    ) {
        this.elementresidences = elementresidences;
    }


    public List<ElementResidence> getElementresidences() {
        return elementresidences;
    }

    public void addElementresidence(Elementresidence elementresidence) {
        this.elementresidences.add(elementresidence);
    }

}