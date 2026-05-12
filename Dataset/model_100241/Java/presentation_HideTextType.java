





import java.util.List;
import java.util.ArrayList;

public class presentation_HideTextType  {

    private String delay;
    private String pathId;
    private String startScale;
    private String direction;
    private String shapeId;
    private String speed;
    private String effect;





    private presentation_SoundType presentation_soundtype;


    public presentation_HideTextType(
        String delay,        String pathId,        String startScale,        String direction,        String shapeId,        String speed,        String effect    ) {
        this.delay = delay;
        this.pathId = pathId;
        this.startScale = startScale;
        this.direction = direction;
        this.shapeId = shapeId;
        this.speed = speed;
        this.effect = effect;
    }


    public String getDelay() {
        return delay;
    }

    public void setDelay(String delay) {
        this.delay = delay;
    }
    public String getPathid() {
        return pathId;
    }

    public void setPathid(String pathId) {
        this.pathId = pathId;
    }
    public String getStartscale() {
        return startScale;
    }

    public void setStartscale(String startScale) {
        this.startScale = startScale;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getShapeid() {
        return shapeId;
    }

    public void setShapeid(String shapeId) {
        this.shapeId = shapeId;
    }
    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }

    public presentation_SoundType getPresentation_soundtype() {
        return presentation_soundtype;
    }

    public void setPresentation_soundtype(presentation_SoundType presentation_soundtype) {
        this.presentation_soundtype = presentation_soundtype;
    }

}