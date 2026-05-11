





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_Pdxmesh  {

    private boolean scaleOnCullDistance;
    private float scale;
    private float cullDistance;
    private String name;
    private String actorFile;



    public ck2gfx_Pdxmesh(
        boolean scaleOnCullDistance,        float scale,        float cullDistance,        String name,        String actorFile    ) {
        this.scaleOnCullDistance = scaleOnCullDistance;
        this.scale = scale;
        this.cullDistance = cullDistance;
        this.name = name;
        this.actorFile = actorFile;
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
    public float getCulldistance() {
        return cullDistance;
    }

    public void setCulldistance(float cullDistance) {
        this.cullDistance = cullDistance;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getActorfile() {
        return actorFile;
    }

    public void setActorfile(String actorFile) {
        this.actorFile = actorFile;
    }


}