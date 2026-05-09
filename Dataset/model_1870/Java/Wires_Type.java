





import java.util.List;
import java.util.ArrayList;

public class Wires_Type extends ConnectableElement {

    private String path;





    private Wires_TypedElement wires_typedelement;


    public Wires_Type(
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

    public Wires_TypedElement getWires_typedelement() {
        return wires_typedelement;
    }

    public void setWires_typedelement(Wires_TypedElement wires_typedelement) {
        this.wires_typedelement = wires_typedelement;
    }

}