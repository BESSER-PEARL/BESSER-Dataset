





import java.util.List;
import java.util.ArrayList;

public class opf_Manifest  {






    private List<opf_Item> opf_items;




    private opf_Package opf_package;


    public opf_Manifest(
    ) {
        this.opf_items = new ArrayList<>();
    }

    public opf_Manifest(
        ArrayList<opf_Item> opf_items    ) {
        this.opf_items = opf_items;
    }


    public List<opf_Item> getOpf_items() {
        return opf_items;
    }

    public void addOpf_item(Opf_item opf_item) {
        this.opf_items.add(opf_item);
    }
    public opf_Package getOpf_package() {
        return opf_package;
    }

    public void setOpf_package(opf_Package opf_package) {
        this.opf_package = opf_package;
    }

}