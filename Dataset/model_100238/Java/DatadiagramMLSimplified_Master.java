





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLSimplified_Master extends UniqueIdElt, IdentifiedElt, NamedElt {

    private String matchByName;
    private String iconSize;
    private String alignName;
    private String hidden;
    private String iconUpdate;
    private String prompt;
    private String patternFlags;
    private String baseID;





    private MastersCollection masterscollection;


    public DatadiagramMLSimplified_Master(
        String matchByName,        String iconSize,        String alignName,        String hidden,        String iconUpdate,        String prompt,        String patternFlags,        String baseID    ) {
        super(
        );
        this.matchByName = matchByName;
        this.iconSize = iconSize;
        this.alignName = alignName;
        this.hidden = hidden;
        this.iconUpdate = iconUpdate;
        this.prompt = prompt;
        this.patternFlags = patternFlags;
        this.baseID = baseID;
    }


    public String getMatchbyname() {
        return matchByName;
    }

    public void setMatchbyname(String matchByName) {
        this.matchByName = matchByName;
    }
    public String getIconsize() {
        return iconSize;
    }

    public void setIconsize(String iconSize) {
        this.iconSize = iconSize;
    }
    public String getAlignname() {
        return alignName;
    }

    public void setAlignname(String alignName) {
        this.alignName = alignName;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getIconupdate() {
        return iconUpdate;
    }

    public void setIconupdate(String iconUpdate) {
        this.iconUpdate = iconUpdate;
    }
    public String getPrompt() {
        return prompt;
    }

    public void setPrompt(String prompt) {
        this.prompt = prompt;
    }
    public String getPatternflags() {
        return patternFlags;
    }

    public void setPatternflags(String patternFlags) {
        this.patternFlags = patternFlags;
    }
    public String getBaseid() {
        return baseID;
    }

    public void setBaseid(String baseID) {
        this.baseID = baseID;
    }

    public MastersCollection getMasterscollection() {
        return masterscollection;
    }

    public void setMasterscollection(MastersCollection masterscollection) {
        this.masterscollection = masterscollection;
    }

}