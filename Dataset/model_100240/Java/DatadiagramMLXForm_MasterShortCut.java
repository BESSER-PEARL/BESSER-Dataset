





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_MasterShortCut extends NamedElt, IdentifiedElt {

    private String alignName;
    private String shortcutHelp;
    private String iconSize;
    private String prompt;
    private String patternFlags;
    private String shortcutURL;





    private List<Icon> icons;


    public DatadiagramMLXForm_MasterShortCut(
        String alignName,        String shortcutHelp,        String iconSize,        String prompt,        String patternFlags,        String shortcutURL    ) {
        super(
        );
        this.alignName = alignName;
        this.shortcutHelp = shortcutHelp;
        this.iconSize = iconSize;
        this.prompt = prompt;
        this.patternFlags = patternFlags;
        this.shortcutURL = shortcutURL;
        this.icons = new ArrayList<>();
    }

    public DatadiagramMLXForm_MasterShortCut(
        String alignName,        String shortcutHelp,        String iconSize,        String prompt,        String patternFlags,        String shortcutURL        ArrayList<Icon> icons    ) {
        this.alignName = alignName;
        this.shortcutHelp = shortcutHelp;
        this.iconSize = iconSize;
        this.prompt = prompt;
        this.patternFlags = patternFlags;
        this.shortcutURL = shortcutURL;
        this.icons = icons;
    }

    public String getAlignname() {
        return alignName;
    }

    public void setAlignname(String alignName) {
        this.alignName = alignName;
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
    public String getShortcuturl() {
        return shortcutURL;
    }

    public void setShortcuturl(String shortcutURL) {
        this.shortcutURL = shortcutURL;
    }

    public List<Icon> getIcons() {
        return icons;
    }

    public void addIcon(Icon icon) {
        this.icons.add(icon);
    }

}