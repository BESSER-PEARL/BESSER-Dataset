





import java.util.List;
import java.util.ArrayList;

public class docbook_TitledElement extends Identifiable {

    private String title;



    public docbook_TitledElement(
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