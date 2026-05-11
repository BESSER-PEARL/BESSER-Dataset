





import java.util.List;
import java.util.ArrayList;

public class smalluml_Enumeration extends ElementNomme, ElementDiagramme, Type {

    private String elements;



    public smalluml_Enumeration(
        String elements    ) {
        super(
        );
        this.elements = elements;
    }


    public String getElements() {
        return elements;
    }

    public void setElements(String elements) {
        this.elements = elements;
    }


}