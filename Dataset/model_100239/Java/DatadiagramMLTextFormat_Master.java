





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_Master extends IdentifiedElt, NamedElt, UniqueIdElt {

    private String prompt;
    private String baseID;
    private String iconUpdate;
    private String iconSize;
    private String matchByName;
    private String patternFlags;
    private String hidden;
    private String alignName;



    public DatadiagramMLTextFormat_Master(
        String prompt,        String baseID,        String iconUpdate,        String iconSize,        String matchByName,        String patternFlags,        String hidden,        String alignName    ) {
        super(
        );
        this.prompt = prompt;
        this.baseID = baseID;
        this.iconUpdate = iconUpdate;
        this.iconSize = iconSize;
        this.matchByName = matchByName;
        this.patternFlags = patternFlags;
        this.hidden = hidden;
        this.alignName = alignName;
    }


    public String getPrompt() {
        return prompt;
    }

    public void setPrompt(String prompt) {
        this.prompt = prompt;
    }
    public String getBaseid() {
        return baseID;
    }

    public void setBaseid(String baseID) {
        this.baseID = baseID;
    }
    public String getIconupdate() {
        return iconUpdate;
    }

    public void setIconupdate(String iconUpdate) {
        this.iconUpdate = iconUpdate;
    }
    public String getIconsize() {
        return iconSize;
    }

    public void setIconsize(String iconSize) {
        this.iconSize = iconSize;
    }
    public String getMatchbyname() {
        return matchByName;
    }

    public void setMatchbyname(String matchByName) {
        this.matchByName = matchByName;
    }
    public String getPatternflags() {
        return patternFlags;
    }

    public void setPatternflags(String patternFlags) {
        this.patternFlags = patternFlags;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getAlignname() {
        return alignName;
    }

    public void setAlignname(String alignName) {
        this.alignName = alignName;
    }


}