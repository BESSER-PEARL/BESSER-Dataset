





import java.util.List;
import java.util.ArrayList;

public class library_Tolerance extends Base {

    private String name;
    private String level;



    public library_Tolerance(
        String name,        String level    ) {
        super(
        );
        this.name = name;
        this.level = level;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }


}