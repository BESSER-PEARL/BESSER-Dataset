





import java.util.List;
import java.util.ArrayList;

public class notation_Image extends GraphicalElement {

    private String path;





    private notation_GraphicalElement notation_graphicalelement;


    public notation_Image(
        String path    ) {
        super(
        );
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public notation_GraphicalElement getNotation_graphicalelement() {
        return notation_graphicalelement;
    }

    public void setNotation_graphicalelement(notation_GraphicalElement notation_graphicalelement) {
        this.notation_graphicalelement = notation_graphicalelement;
    }

}