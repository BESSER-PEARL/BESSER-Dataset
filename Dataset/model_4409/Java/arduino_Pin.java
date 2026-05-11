





import java.util.List;
import java.util.ArrayList;

public class arduino_Pin extends NamedElement {

    private int level;



    public arduino_Pin(
        int level    ) {
        super(
        );
        this.level = level;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }


}