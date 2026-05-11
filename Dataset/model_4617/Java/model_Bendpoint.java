





import java.util.List;
import java.util.ArrayList;

public class model_Bendpoint extends OnoObject {

    private int posY;
    private int posX;





    private model_Edge model_edge;


    public model_Bendpoint(
        int posY,        int posX    ) {
        super(
        );
        this.posY = posY;
        this.posX = posX;
    }


    public int getPosy() {
        return posY;
    }

    public void setPosy(int posY) {
        this.posY = posY;
    }
    public int getPosx() {
        return posX;
    }

    public void setPosx(int posX) {
        this.posX = posX;
    }

    public model_Edge getModel_edge() {
        return model_edge;
    }

    public void setModel_edge(model_Edge model_edge) {
        this.model_edge = model_edge;
    }

}