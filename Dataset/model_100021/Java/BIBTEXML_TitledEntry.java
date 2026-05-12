





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_TitledEntry extends Entry {

    private String title;



    public BIBTEXML_TitledEntry(
        String title    ) {
        super(
        );
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}