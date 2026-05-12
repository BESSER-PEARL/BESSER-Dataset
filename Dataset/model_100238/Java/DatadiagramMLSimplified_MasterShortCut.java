





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLSimplified_MasterShortCut extends IdentifiedElt, NamedElt {

    private String shortcutHelp;
    private String patternFlags;
    private String alignName;
    private String prompt;
    private String iconSize;
    private String shortcutURL;





    private MastersCollection masterscollection;




    private List<Icon> icons;


    public DatadiagramMLSimplified_MasterShortCut(
        String shortcutHelp,        String patternFlags,        String alignName,        String prompt,        String iconSize,        String shortcutURL    ) {
        super(
        );
        this.shortcutHelp = shortcutHelp;
        this.patternFlags = patternFlags;
        this.alignName = alignName;
        this.prompt = prompt;
        this.iconSize = iconSize;
        this.shortcutURL = shortcutURL;
        this.icons = new ArrayList<>();
    }

    public DatadiagramMLSimplified_MasterShortCut(
        String shortcutHelp,        String patternFlags,        String alignName,        String prompt,        String iconSize,        String shortcutURL        ArrayList<Icon> icons    ) {
        this.shortcutHelp = shortcutHelp;
        this.patternFlags = patternFlags;
        this.alignName = alignName;
        this.prompt = prompt;
        this.iconSize = iconSize;
        this.shortcutURL = shortcutURL;
        this.icons = icons;
    }

    public String getShortcuthelp() {
        return shortcutHelp;
    }

    public void setShortcuthelp(String shortcutHelp) {
        this.shortcutHelp = shortcutHelp;
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
    public String getPrompt() {
        return prompt;
    }

    public void setPrompt(String prompt) {
        this.prompt = prompt;
    }
    public String getIconsize() {
        return iconSize;
    }

    public void setIconsize(String iconSize) {
        this.iconSize = iconSize;
    }
    public String getShortcuturl() {
        return shortcutURL;
    }

    public void setShortcuturl(String shortcutURL) {
        this.shortcutURL = shortcutURL;
    }

    public MastersCollection getMasterscollection() {
        return masterscollection;
    }

    public void setMasterscollection(MastersCollection masterscollection) {
        this.masterscollection = masterscollection;
    }
    public List<Icon> getIcons() {
        return icons;
    }

    public void addIcon(Icon icon) {
        this.icons.add(icon);
    }

}