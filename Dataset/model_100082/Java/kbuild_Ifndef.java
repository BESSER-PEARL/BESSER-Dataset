





import java.util.List;
import java.util.ArrayList;

public class kbuild_Ifndef extends BuildEntry {

    private String name;



    public kbuild_Ifndef(
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