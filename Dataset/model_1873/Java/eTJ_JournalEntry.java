





import java.util.List;
import java.util.ArrayList;

public class eTJ_JournalEntry extends ResourceAttribute, ProjectAttribute {

    private String headline;



    public eTJ_JournalEntry(
        String headline    ) {
        super(
        );
        this.headline = headline;
    }


    public String getHeadline() {
        return headline;
    }

    public void setHeadline(String headline) {
        this.headline = headline;
    }


}