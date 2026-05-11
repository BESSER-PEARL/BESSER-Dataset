





import java.util.List;
import java.util.ArrayList;

public class dsl_ParticleActor extends Actor {

    private String startVariation;
    private int perSecond;
    private String minLife;
    private int maxCount;
    private int duration;
    private String maxLife;
    private String add;
    private int nbRow;
    private int nbCol;
    private String spritePath;
    private String startSize;
    private String endSize;
    private String directionBone;
    private String emissionBone;



    public dsl_ParticleActor(
        String startVariation,        int perSecond,        String minLife,        int maxCount,        int duration,        String maxLife,        String add,        int nbRow,        int nbCol,        String spritePath,        String startSize,        String endSize,        String directionBone,        String emissionBone    ) {
        super(
        );
        this.startVariation = startVariation;
        this.perSecond = perSecond;
        this.minLife = minLife;
        this.maxCount = maxCount;
        this.duration = duration;
        this.maxLife = maxLife;
        this.add = add;
        this.nbRow = nbRow;
        this.nbCol = nbCol;
        this.spritePath = spritePath;
        this.startSize = startSize;
        this.endSize = endSize;
        this.directionBone = directionBone;
        this.emissionBone = emissionBone;
    }


    public String getStartvariation() {
        return startVariation;
    }

    public void setStartvariation(String startVariation) {
        this.startVariation = startVariation;
    }
    public int getPersecond() {
        return perSecond;
    }

    public void setPersecond(int perSecond) {
        this.perSecond = perSecond;
    }
    public String getMinlife() {
        return minLife;
    }

    public void setMinlife(String minLife) {
        this.minLife = minLife;
    }
    public int getMaxcount() {
        return maxCount;
    }

    public void setMaxcount(int maxCount) {
        this.maxCount = maxCount;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public String getMaxlife() {
        return maxLife;
    }

    public void setMaxlife(String maxLife) {
        this.maxLife = maxLife;
    }
    public String getAdd() {
        return add;
    }

    public void setAdd(String add) {
        this.add = add;
    }
    public int getNbrow() {
        return nbRow;
    }

    public void setNbrow(int nbRow) {
        this.nbRow = nbRow;
    }
    public int getNbcol() {
        return nbCol;
    }

    public void setNbcol(int nbCol) {
        this.nbCol = nbCol;
    }
    public String getSpritepath() {
        return spritePath;
    }

    public void setSpritepath(String spritePath) {
        this.spritePath = spritePath;
    }
    public String getStartsize() {
        return startSize;
    }

    public void setStartsize(String startSize) {
        this.startSize = startSize;
    }
    public String getEndsize() {
        return endSize;
    }

    public void setEndsize(String endSize) {
        this.endSize = endSize;
    }
    public String getDirectionbone() {
        return directionBone;
    }

    public void setDirectionbone(String directionBone) {
        this.directionBone = directionBone;
    }
    public String getEmissionbone() {
        return emissionBone;
    }

    public void setEmissionbone(String emissionBone) {
        this.emissionBone = emissionBone;
    }


}