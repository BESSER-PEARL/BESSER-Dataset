





import java.util.List;
import java.util.ArrayList;

public class SPL_NamedBranch extends Branch {

    private String name;



    public SPL_NamedBranch(
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