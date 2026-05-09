





import java.util.List;
import java.util.ArrayList;

public class Arch_DropDownList extends GraphicControl {

    private String items;



    public Arch_DropDownList(
        String items    ) {
        super(
        );
        this.items = items;
    }


    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }


}