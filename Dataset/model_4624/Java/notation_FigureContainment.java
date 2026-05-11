





import java.util.List;
import java.util.ArrayList;

public class notation_FigureContainment  {

    private String layout;





    private List<notation_GraphicalElement> notation_graphicalelements;




    private notation_Figure notation_figure;


    public notation_FigureContainment(
        String layout    ) {
        this.layout = layout;
        this.notation_graphicalelements = new ArrayList<>();
    }

    public notation_FigureContainment(
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

    public List<notation_GraphicalElement> getNotation_graphicalelements() {
        return notation_graphicalelements;
    }

    public void addNotation_graphicalelement(Notation_graphicalelement notation_graphicalelement) {
        this.notation_graphicalelements.add(notation_graphicalelement);
    }
    public notation_Figure getNotation_figure() {
        return notation_figure;
    }

    public void setNotation_figure(notation_Figure notation_figure) {
        this.notation_figure = notation_figure;
    }

}