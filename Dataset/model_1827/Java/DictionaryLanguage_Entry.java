





import java.util.List;
import java.util.ArrayList;

public class DictionaryLanguage_Entry  {

    private String content;
    private String level;



    public DictionaryLanguage_Entry(
        String content,        String level    ) {
        this.content = content;
        this.level = level;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }


}