





import java.util.List;
import java.util.ArrayList;

public class setup_KeyBindingTask extends SetupTask {

    private String command;
    private String scheme;
    private String keys;
    private String platform;
    private String locale;



    public setup_KeyBindingTask(
        String command,        String scheme,        String keys,        String platform,        String locale    ) {
        super(
        );
        this.command = command;
        this.scheme = scheme;
        this.keys = keys;
        this.platform = platform;
        this.locale = locale;
    }


    public String getCommand() {
        return command;
    }

    public void setCommand(String command) {
        this.command = command;
    }
    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }
    public String getKeys() {
        return keys;
    }

    public void setKeys(String keys) {
        this.keys = keys;
    }
    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }


}