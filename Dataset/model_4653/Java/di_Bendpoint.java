





import java.util.List;
import java.util.ArrayList;

public class di_Bendpoint  {

    private String targetX;
    private String targetY;
    private String sourceX;
    private String sourceY;



    public di_Bendpoint(
        String targetX,        String targetY,        String sourceX,        String sourceY    ) {
        this.targetX = targetX;
        this.targetY = targetY;
        this.sourceX = sourceX;
        this.sourceY = sourceY;
    }


    public String getTargetx() {
        return targetX;
    }

    public void setTargetx(String targetX) {
        this.targetX = targetX;
    }
    public String getTargety() {
        return targetY;
    }

    public void setTargety(String targetY) {
        this.targetY = targetY;
    }
    public String getSourcex() {
        return sourceX;
    }

    public void setSourcex(String sourceX) {
        this.sourceX = sourceX;
    }
    public String getSourcey() {
        return sourceY;
    }

    public void setSourcey(String sourceY) {
        this.sourceY = sourceY;
    }


}