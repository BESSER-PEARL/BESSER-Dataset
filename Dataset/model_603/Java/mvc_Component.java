





import java.util.List;
import java.util.ArrayList;

public class mvc_Component extends Annotable {

    private String name;



    public mvc_Component(
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