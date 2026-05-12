





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_Master extends NamedElt, UniqueIdElt, IdentifiedElt {

    private String baseID;
    private String iconSize;
    private String matchByName;
    private String iconUpdate;
    private String prompt;
    private String patternFlags;
    private String alignName;
    private String hidden;





    private MastersCollection masterscollection;


    public DatadiagramMLBasicDef_Master(
        String baseID,        String iconSize,        String matchByName,        String iconUpdate,        String prompt,        String patternFlags,        String alignName,        String hidden    ) {
        super(
        );
        this.baseID = baseID;
        this.iconSize = iconSize;
        this.matchByName = matchByName;
        this.iconUpdate = iconUpdate;
        this.prompt = prompt;
        this.patternFlags = patternFlags;
        this.alignName = alignName;
        this.hidden = hidden;
    }


    public String getBaseid() {
        return baseID;
    }

    public void setBaseid(String baseID) {
        this.baseID = baseID;
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

    public MastersCollection getMasterscollection() {
        return masterscollection;
    }

    public void setMasterscollection(MastersCollection masterscollection) {
        this.masterscollection = masterscollection;
    }

}