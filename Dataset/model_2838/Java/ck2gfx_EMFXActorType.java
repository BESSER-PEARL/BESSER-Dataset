





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_EMFXActorType  {

    private String idle;
    private float cullDistance;
    private String actorFile;
    private String name;
    private String attack;
    private boolean scaleOnCullDistance;
    private float scale;
    private String move;
    private boolean useAnimation;



    public ck2gfx_EMFXActorType(
        String idle,        float cullDistance,        String actorFile,        String name,        String attack,        boolean scaleOnCullDistance,        float scale,        String move,        boolean useAnimation    ) {
        this.idle = idle;
        this.cullDistance = cullDistance;
        this.actorFile = actorFile;
        this.name = name;
        this.attack = attack;
        this.scaleOnCullDistance = scaleOnCullDistance;
        this.scale = scale;
        this.move = move;
        this.useAnimation = useAnimation;
    }


    public String getIdle() {
        return idle;
    }

    public void setIdle(String idle) {
        this.idle = idle;
    }
    public float getCulldistance() {
        return cullDistance;
    }

    public void setCulldistance(float cullDistance) {
        this.cullDistance = cullDistance;
    }
    public String getActorfile() {
        return actorFile;
    }

    public void setActorfile(String actorFile) {
        this.actorFile = actorFile;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAttack() {
        return attack;
    }

    public void setAttack(String attack) {
        this.attack = attack;
    }
    public boolean getScaleonculldistance() {
        return scaleOnCullDistance;
    }

    public void setScaleonculldistance(boolean scaleOnCullDistance) {
        this.scaleOnCullDistance = scaleOnCullDistance;
    }
    public float getScale() {
        return scale;
    }

    public void setScale(float scale) {
        this.scale = scale;
    }
    public String getMove() {
        return move;
    }

    public void setMove(String move) {
        this.move = move;
    }
    public boolean getUseanimation() {
        return useAnimation;
    }

    public void setUseanimation(boolean useAnimation) {
        this.useAnimation = useAnimation;
    }


}