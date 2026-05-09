





import java.util.List;
import java.util.ArrayList;

public class notation_RelativeBendPoint extends BendPoint {

    private int targetX;
    private int sourceY;
    private int targetY;
    private int sourceX;



    public notation_RelativeBendPoint(
        int targetX,        int sourceY,        int targetY,        int sourceX    ) {
        super(
        );
        this.targetX = targetX;
        this.sourceY = sourceY;
        this.targetY = targetY;
        this.sourceX = sourceX;
    }


    public int getTargetx() {
        return targetX;
    }

    public void setTargetx(int targetX) {
        this.targetX = targetX;
    }
    public int getSourcey() {
        return sourceY;
    }

    public void setSourcey(int sourceY) {
        this.sourceY = sourceY;
    }
    public int getTargety() {
        return targetY;
    }

    public void setTargety(int targetY) {
        this.targetY = targetY;
    }
    public int getSourcex() {
        return sourceX;
    }

    public void setSourcex(int sourceX) {
        this.sourceX = sourceX;
    }


}