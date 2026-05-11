





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelBendpoint extends Cloneable {

    private int endX;
    private int endY;
    private int startX;
    private int startY;





    private model_DiagramModelConnection model_diagrammodelconnection;


    public model_DiagramModelBendpoint(
        int endX,        int endY,        int startX,        int startY    ) {
        super(
        );
        this.endX = endX;
        this.endY = endY;
        this.startX = startX;
        this.startY = startY;
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
    public int getStartx() {
        return startX;
    }

    public void setStartx(int startX) {
        this.startX = startX;
    }
    public int getStarty() {
        return startY;
    }

    public void setStarty(int startY) {
        this.startY = startY;
    }

    public model_DiagramModelConnection getModel_diagrammodelconnection() {
        return model_diagrammodelconnection;
    }

    public void setModel_diagrammodelconnection(model_DiagramModelConnection model_diagrammodelconnection) {
        this.model_diagrammodelconnection = model_diagrammodelconnection;
    }

}