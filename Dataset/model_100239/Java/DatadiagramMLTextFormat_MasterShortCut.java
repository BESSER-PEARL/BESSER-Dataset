





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_MasterShortCut extends NamedElt, IdentifiedElt {

    private String prompt;
    private String alignName;
    private String patternFlags;
    private String shortcutHelp;
    private String iconSize;
    private String shortcutURL;



    public DatadiagramMLTextFormat_MasterShortCut(
        String prompt,        String alignName,        String patternFlags,        String shortcutHelp,        String iconSize,        String shortcutURL    ) {
        super(
        );
        this.prompt = prompt;
        this.alignName = alignName;
        this.patternFlags = patternFlags;
        this.shortcutHelp = shortcutHelp;
        this.iconSize = iconSize;
        this.shortcutURL = shortcutURL;
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
    public String getPatternflags() {
        return patternFlags;
    }

    public void setPatternflags(String patternFlags) {
        this.patternFlags = patternFlags;
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
    public String getShortcuturl() {
        return shortcutURL;
    }

    public void setShortcuturl(String shortcutURL) {
        this.shortcutURL = shortcutURL;
    }


}