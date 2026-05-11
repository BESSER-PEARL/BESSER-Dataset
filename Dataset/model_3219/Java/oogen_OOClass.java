





import java.util.List;
import java.util.ArrayList;

public class oogen_OOClass extends OOCommentOwner {

    private boolean keep;
    private String name;
    private String languages;



    public oogen_OOClass(
        boolean keep,        String name,        String languages    ) {
        super(
        );
        this.keep = keep;
        this.name = name;
        this.languages = languages;
    }


    public boolean getKeep() {
        return keep;
    }

    public void setKeep(boolean keep) {
        this.keep = keep;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLanguages() {
        return languages;
    }

    public void setLanguages(String languages) {
        this.languages = languages;
    }


}