





import java.util.List;
import java.util.ArrayList;

public class ric_Heading extends ClassifiableComponent, EventComponent, IdentifiableComponent, InlineComponent {

    private String level;



    public ric_Heading(
        String level    ) {
        super(
        );
        this.level = level;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }


}