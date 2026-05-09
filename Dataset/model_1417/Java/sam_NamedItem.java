





import java.util.List;
import java.util.ArrayList;

public class sam_NamedItem extends IdentifiedItem {

    private String name;



    public sam_NamedItem(
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