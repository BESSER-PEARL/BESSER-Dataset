





import java.util.List;
import java.util.ArrayList;

public class mvc_Model extends Annotable {

    private String name;



    public mvc_Model(
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