





import java.util.List;
import java.util.ArrayList;

public class becontent_ApplyItem extends ApplyCommand {

    private String key;
    private String prefix;



    public becontent_ApplyItem(
        String key,        String prefix    ) {
        super(
        );
        this.key = key;
        this.prefix = prefix;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}