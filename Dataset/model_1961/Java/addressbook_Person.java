





import java.util.List;
import java.util.ArrayList;

public class addressbook_Person extends Contact {

    private String Title;



    public addressbook_Person(
        String Title    ) {
        super(
        );
        this.Title = Title;
    }


    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }


}