





import java.util.List;
import java.util.ArrayList;

public class notation_Node extends DiagramElement {






    private notation_Compartment notation_compartment;




    private notation_GraphicalElement notation_graphicalelement;


    public notation_Node(
    ) {
        super(
        );
    }



    public notation_Compartment getNotation_compartment() {
        return notation_compartment;
    }

    public void setNotation_compartment(notation_Compartment notation_compartment) {
        this.notation_compartment = notation_compartment;
    }
    public notation_GraphicalElement getNotation_graphicalelement() {
        return notation_graphicalelement;
    }

    public void setNotation_graphicalelement(notation_GraphicalElement notation_graphicalelement) {
        this.notation_graphicalelement = notation_graphicalelement;
    }

}