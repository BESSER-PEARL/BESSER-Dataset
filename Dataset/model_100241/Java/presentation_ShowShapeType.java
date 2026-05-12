





import java.util.List;
import java.util.ArrayList;

public class presentation_ShowShapeType  {

    private String direction;
    private String pathId;
    private String speed;
    private String startScale;
    private String effect;
    private String shapeId;
    private String delay;





    private presentation_SoundType presentation_soundtype;


    public presentation_ShowShapeType(
        String direction,        String pathId,        String speed,        String startScale,        String effect,        String shapeId,        String delay    ) {
        this.direction = direction;
        this.pathId = pathId;
        this.speed = speed;
        this.startScale = startScale;
        this.effect = effect;
        this.shapeId = shapeId;
        this.delay = delay;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getPathid() {
        return pathId;
    }

    public void setPathid(String pathId) {
        this.pathId = pathId;
    }
    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getStartscale() {
        return startScale;
    }

    public void setStartscale(String startScale) {
        this.startScale = startScale;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public String getShapeid() {
        return shapeId;
    }

    public void setShapeid(String shapeId) {
        this.shapeId = shapeId;
    }
    public String getDelay() {
        return delay;
    }

    public void setDelay(String delay) {
        this.delay = delay;
    }

    public presentation_SoundType getPresentation_soundtype() {
        return presentation_soundtype;
    }

    public void setPresentation_soundtype(presentation_SoundType presentation_soundtype) {
        this.presentation_soundtype = presentation_soundtype;
    }

}