





import java.util.List;
import java.util.ArrayList;

public class presentation_HideShapeType  {

    private String delay;
    private String shapeId;
    private String direction;
    private String startScale;
    private String effect;
    private String pathId;
    private String speed;





    private presentation_SoundType presentation_soundtype;


    public presentation_HideShapeType(
        String delay,        String shapeId,        String direction,        String startScale,        String effect,        String pathId,        String speed    ) {
        this.delay = delay;
        this.shapeId = shapeId;
        this.direction = direction;
        this.startScale = startScale;
        this.effect = effect;
        this.pathId = pathId;
        this.speed = speed;
    }


    public String getDelay() {
        return delay;
    }

    public void setDelay(String delay) {
        this.delay = delay;
    }
    public String getShapeid() {
        return shapeId;
    }

    public void setShapeid(String shapeId) {
        this.shapeId = shapeId;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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

    public presentation_SoundType getPresentation_soundtype() {
        return presentation_soundtype;
    }

    public void setPresentation_soundtype(presentation_SoundType presentation_soundtype) {
        this.presentation_soundtype = presentation_soundtype;
    }

}