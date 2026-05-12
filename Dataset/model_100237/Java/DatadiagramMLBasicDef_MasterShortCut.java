





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_MasterShortCut extends NamedElt, IdentifiedElt {

    private String prompt;
    private String alignName;
    private String shortcutURL;
    private String shortcutHelp;
    private String iconSize;
    private String patternFlags;





    private MastersCollection masterscollection;


    public DatadiagramMLBasicDef_MasterShortCut(
        String prompt,        String alignName,        String shortcutURL,        String shortcutHelp,        String iconSize,        String patternFlags    ) {
        super(
        );
        this.prompt = prompt;
        this.alignName = alignName;
        this.shortcutURL = shortcutURL;
        this.shortcutHelp = shortcutHelp;
        this.iconSize = iconSize;
        this.patternFlags = patternFlags;
    }


    public String getPrompt() {
        return prompt;
    }

    public void setPrompt(String prompt) {
        this.prompt = prompt;
    }
    public String getAlignname() {
        return alignName;
    }

    public void setAlignname(String alignName) {
        this.alignName = alignName;
    }
    public String getShortcuturl() {
        return shortcutURL;
    }

    public void setShortcuturl(String shortcutURL) {
        this.shortcutURL = shortcutURL;
    }
    public String getShortcuthelp() {
        return shortcutHelp;
    }

    public void setShortcuthelp(String shortcutHelp) {
        this.shortcutHelp = shortcutHelp;
    }
    public String getIconsize() {
        return iconSize;
    }

    public void setIconsize(String iconSize) {
        this.iconSize = iconSize;
    }
    public String getPatternflags() {
        return patternFlags;
    }

    public void setPatternflags(String patternFlags) {
        this.patternFlags = patternFlags;
    }

    public MastersCollection getMasterscollection() {
        return masterscollection;
    }

    public void setMasterscollection(MastersCollection masterscollection) {
        this.masterscollection = masterscollection;
    }

}