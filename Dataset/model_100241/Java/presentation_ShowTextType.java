





import java.util.List;
import java.util.ArrayList;

public class presentation_ShowTextType  {

    private String effect;
    private String speed;
    private String startScale;
    private String direction;
    private String delay;
    private String pathId;
    private String shapeId;





    private presentation_SoundType presentation_soundtype;


    public presentation_ShowTextType(
        String effect,        String speed,        String startScale,        String direction,        String delay,        String pathId,        String shapeId    ) {
        this.effect = effect;
        this.speed = speed;
        this.startScale = startScale;
        this.direction = direction;
        this.delay = delay;
        this.pathId = pathId;
        this.shapeId = shapeId;
    }


    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
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
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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
    public String getShapeid() {
        return shapeId;
    }

    public void setShapeid(String shapeId) {
        this.shapeId = shapeId;
    }

    public presentation_SoundType getPresentation_soundtype() {
        return presentation_soundtype;
    }

    public void setPresentation_soundtype(presentation_SoundType presentation_soundtype) {
        this.presentation_soundtype = presentation_soundtype;
    }

}