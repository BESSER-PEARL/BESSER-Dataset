





import java.util.List;
import java.util.ArrayList;

public class library_Tolerance extends Base {

    private String level;
    private String name;



    public library_Tolerance(
        String level,        String name    ) {
        super(
        );
        this.level = level;
        this.name = name;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}