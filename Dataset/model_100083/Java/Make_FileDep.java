





import java.util.List;
import java.util.ArrayList;

public class Make_FileDep extends Dependency {

    private String name;



    public Make_FileDep(
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