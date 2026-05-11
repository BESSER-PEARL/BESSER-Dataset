





import java.util.List;
import java.util.ArrayList;

public class dom_SelectObject extends SelectStatement {

    private String name;



    public dom_SelectObject(
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