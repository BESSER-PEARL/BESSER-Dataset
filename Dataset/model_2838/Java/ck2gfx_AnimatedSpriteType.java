





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_AnimatedSpriteType  {

    private String texturefile;
    private String name;
    private float animationRateFps;
    private boolean playOnShow;
    private boolean looping;
    private int noOfFrames;



    public ck2gfx_AnimatedSpriteType(
        String texturefile,        String name,        float animationRateFps,        boolean playOnShow,        boolean looping,        int noOfFrames    ) {
        this.texturefile = texturefile;
        this.name = name;
        this.animationRateFps = animationRateFps;
        this.playOnShow = playOnShow;
        this.looping = looping;
        this.noOfFrames = noOfFrames;
    }


    public String getTexturefile() {
        return texturefile;
    }

    public void setTexturefile(String texturefile) {
        this.texturefile = texturefile;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getAnimationratefps() {
        return animationRateFps;
    }

    public void setAnimationratefps(float animationRateFps) {
        this.animationRateFps = animationRateFps;
    }
    public boolean getPlayonshow() {
        return playOnShow;
    }

    public void setPlayonshow(boolean playOnShow) {
        this.playOnShow = playOnShow;
    }
    public boolean getLooping() {
        return looping;
    }

    public void setLooping(boolean looping) {
        this.looping = looping;
    }
    public int getNoofframes() {
        return noOfFrames;
    }

    public void setNoofframes(int noOfFrames) {
        this.noOfFrames = noOfFrames;
    }


}