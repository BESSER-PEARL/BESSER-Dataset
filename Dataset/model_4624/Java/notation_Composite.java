





import java.util.List;
import java.util.ArrayList;

public class notation_Composite extends GraphicalElement {

    private String layout;





    private notation_GraphicalElement notation_graphicalelement;




    private List<notation_GraphicalElement> notation_graphicalelements;


    public notation_Composite(
        String layout    ) {
        super(
        );
        this.layout = layout;
        this.notation_graphicalelements = new ArrayList<>();
    }

    public notation_Composite(
        String layout        ArrayList<notation_GraphicalElement> notation_graphicalelements    ) {
        this.layout = layout;
        this.notation_graphicalelements = notation_graphicalelements;
    }

    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }

    public notation_GraphicalElement getNotation_graphicalelement() {
        return notation_graphicalelement;
    }

    public void setNotation_graphicalelement(notation_GraphicalElement notation_graphicalelement) {
        this.notation_graphicalelement = notation_graphicalelement;
    }
    public List<notation_GraphicalElement> getNotation_graphicalelements() {
        return notation_graphicalelements;
    }

    public void addNotation_graphicalelement(Notation_graphicalelement notation_graphicalelement) {
        this.notation_graphicalelements.add(notation_graphicalelement);
    }

}