





import java.util.List;
import java.util.ArrayList;

public class xwiki_Translation extends LinkCollection {

    private String language;



    public xwiki_Translation(
        String language    ) {
        super(
        );
        this.language = language;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}