





import java.util.List;
import java.util.ArrayList;

public class ir_ItemType extends IrAnnotable {

    private String name;



    public ir_ItemType(
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