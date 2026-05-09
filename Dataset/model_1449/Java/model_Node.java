





import java.util.List;
import java.util.ArrayList;

public class model_Node  {

    private int posX;
    private int posY;





    private model_Diagram model_diagram;


    public model_Node(
        int posX,        int posY    ) {
        this.posX = posX;
        this.posY = posY;
    }


    public int getPosx() {
        return posX;
    }

    public void setPosx(int posX) {
        this.posX = posX;
    }
    public int getPosy() {
        return posY;
    }

    public void setPosy(int posY) {
        this.posY = posY;
    }

    public model_Diagram getModel_diagram() {
        return model_diagram;
    }

    public void setModel_diagram(model_Diagram model_diagram) {
        this.model_diagram = model_diagram;
    }

}