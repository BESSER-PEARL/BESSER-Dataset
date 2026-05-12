





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_InProceedings extends AuthoredEntry, Proceedings, BookTitledEntry {

    private String pages;



    public BIBTEXML_InProceedings(
        String pages    ) {
        super(
        );
        this.pages = pages;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }


}