





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelBendpoint extends Cloneable {

    private int endX;
    private int endY;
    private int startY;
    private int startX;





    private model_DiagramModelConnection model_diagrammodelconnection;


    public model_DiagramModelBendpoint(
        int endX,        int endY,        int startY,        int startX    ) {
        super(
        );
        this.endX = endX;
        this.endY = endY;
        this.startY = startY;
        this.startX = startX;
    }


    public int getEndx() {
        return endX;
    }

    public void setEndx(int endX) {
        this.endX = endX;
    }
    public int getEndy() {
        return endY;
    }

    public void setEndy(int endY) {
        this.endY = endY;
    }
    public int getStarty() {
        return startY;
    }

    public void setStarty(int startY) {
        this.startY = startY;
    }
    public int getStartx() {
        return startX;
    }

    public void setStartx(int startX) {
        this.startX = startX;
    }

    public model_DiagramModelConnection getModel_diagrammodelconnection() {
        return model_diagrammodelconnection;
    }

    public void setModel_diagrammodelconnection(model_DiagramModelConnection model_diagrammodelconnection) {
        this.model_diagrammodelconnection = model_diagrammodelconnection;
    }

}