





import java.util.List;
import java.util.ArrayList;

public class arduino_Module extends NamedElement {

    private String level;



    public arduino_Module(
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