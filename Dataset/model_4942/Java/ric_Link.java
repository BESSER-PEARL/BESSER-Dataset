





import java.util.List;
import java.util.ArrayList;

public class ric_Link extends ClassifiableComponent, EventComponent, IdentifiableComponent, InlineComponent {

    private String title;



    public ric_Link(
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