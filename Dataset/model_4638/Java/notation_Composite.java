





import java.util.List;
import java.util.ArrayList;

public class notation_Composite extends NotationElement {






    private List<notation_NotationElement> notation_notationelements;


    public notation_Composite(
    ) {
        super(
        );
        this.notation_notationelements = new ArrayList<>();
    }

    public notation_Composite(
        ArrayList<notation_NotationElement> notation_notationelements    ) {
        this.notation_notationelements = notation_notationelements;
    }


    public List<notation_NotationElement> getNotation_notationelements() {
        return notation_notationelements;
    }

    public void addNotation_notationelement(Notation_notationelement notation_notationelement) {
        this.notation_notationelements.add(notation_notationelement);
    }

}