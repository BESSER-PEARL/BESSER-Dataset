





import java.util.List;
import java.util.ArrayList;

public class myDsl_Entity extends Member {

    private String name;



    public myDsl_Entity(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}