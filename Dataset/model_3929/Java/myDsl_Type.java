





import java.util.List;
import java.util.ArrayList;

public class myDsl_Type extends Element {

    private String name;



    public myDsl_Type(
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