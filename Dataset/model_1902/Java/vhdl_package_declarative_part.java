





import java.util.List;
import java.util.ArrayList;

public class vhdl_package_declarative_part  {






    private List<vhdl_package_declarative_item> vhdl_package_declarative_items;


    public vhdl_package_declarative_part(
    ) {
        this.vhdl_package_declarative_items = new ArrayList<>();
    }

    public vhdl_package_declarative_part(
        ArrayList<vhdl_package_declarative_item> vhdl_package_declarative_items    ) {
        this.vhdl_package_declarative_items = vhdl_package_declarative_items;
    }


    public List<vhdl_package_declarative_item> getVhdl_package_declarative_items() {
        return vhdl_package_declarative_items;
    }

    public void addVhdl_package_declarative_item(Vhdl_package_declarative_item vhdl_package_declarative_item) {
        this.vhdl_package_declarative_items.add(vhdl_package_declarative_item);
    }

}