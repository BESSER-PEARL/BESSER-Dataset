





import java.util.List;
import java.util.ArrayList;

public class xwiki_Tag extends LinkCollection {

    private String name;



    public xwiki_Tag(
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