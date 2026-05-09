





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Text extends Control {

    private String name;



    public appBuilderDSL_Text(
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