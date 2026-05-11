





import java.util.List;
import java.util.ArrayList;

public class model_EnumValue extends Value {

    private String name;



    public model_EnumValue(
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