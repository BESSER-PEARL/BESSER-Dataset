





import java.util.List;
import java.util.ArrayList;

public class bibtex_TitledEntry extends BibTeXEntry {

    private String title;



    public bibtex_TitledEntry(
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