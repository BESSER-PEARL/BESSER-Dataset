





import java.util.List;
import java.util.ArrayList;

public class drn_Option  {

    private String name;





    private drn_With drn_with;


    public drn_Option(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public drn_With getDrn_with() {
        return drn_with;
    }

    public void setDrn_with(drn_With drn_with) {
        this.drn_with = drn_with;
    }

}