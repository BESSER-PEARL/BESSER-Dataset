





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_Master extends NamedElt, UniqueIdElt, IdentifiedElt {

    private String iconSize;
    private String matchByName;
    private String alignName;
    private String patternFlags;
    private String hidden;
    private String baseID;
    private String prompt;
    private String iconUpdate;



    public DatadiagramMLXForm_Master(
        String iconSize,        String matchByName,        String alignName,        String patternFlags,        String hidden,        String baseID,        String prompt,        String iconUpdate    ) {
        super(
        );
        this.iconSize = iconSize;
        this.matchByName = matchByName;
        this.alignName = alignName;
        this.patternFlags = patternFlags;
        this.hidden = hidden;
        this.baseID = baseID;
        this.prompt = prompt;
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
    public String getAlignname() {
        return alignName;
    }

    public void setAlignname(String alignName) {
        this.alignName = alignName;
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
    public String getBaseid() {
        return baseID;
    }

    public void setBaseid(String baseID) {
        this.baseID = baseID;
    }
    public String getPrompt() {
        return prompt;
    }

    public void setPrompt(String prompt) {
        this.prompt = prompt;
    }
    public String getIconupdate() {
        return iconUpdate;
    }

    public void setIconupdate(String iconUpdate) {
        this.iconUpdate = iconUpdate;
    }


}