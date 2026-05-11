





import java.util.List;
import java.util.ArrayList;

public class ric_Heading extends InlineComponent, IdentifiableComponent, EventComponent, ClassifiableComponent {

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