





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Label extends Control {

    private String name;



    public appBuilderDSL_Label(
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