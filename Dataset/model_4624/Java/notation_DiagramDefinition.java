





import java.util.List;
import java.util.ArrayList;

public class notation_DiagramDefinition  {

    private boolean allowChunks;
    private String targetedAudience;
    private int Level;
    private String Legend;





    private notation_NotationDefinition notation_notationdefinition;


    public notation_DiagramDefinition(
        boolean allowChunks,        String targetedAudience,        int Level,        String Legend    ) {
        this.allowChunks = allowChunks;
        this.targetedAudience = targetedAudience;
        this.Level = Level;
        this.Legend = Legend;
    }


    public boolean getAllowchunks() {
        return allowChunks;
    }

    public void setAllowchunks(boolean allowChunks) {
        this.allowChunks = allowChunks;
    }
    public String getTargetedaudience() {
        return targetedAudience;
    }

    public void setTargetedaudience(String targetedAudience) {
        this.targetedAudience = targetedAudience;
    }
    public int getLevel() {
        return Level;
    }

    public void setLevel(int Level) {
        this.Level = Level;
    }
    public String getLegend() {
        return Legend;
    }

    public void setLegend(String Legend) {
        this.Legend = Legend;
    }

    public notation_NotationDefinition getNotation_notationdefinition() {
        return notation_notationdefinition;
    }

    public void setNotation_notationdefinition(notation_NotationDefinition notation_notationdefinition) {
        this.notation_notationdefinition = notation_notationdefinition;
    }

}