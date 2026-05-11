





import java.util.List;
import java.util.ArrayList;

public class nestedgroup_A  {

    private String name;
    private String b;
    private String group;





    private List<nestedgroup_CType> nestedgroup_ctypes;


    public nestedgroup_A(
        String name,        String b,        String group    ) {
        this.name = name;
        this.b = b;
        this.group = group;
        this.nestedgroup_ctypes = new ArrayList<>();
    }

    public nestedgroup_A(
        String name,        String b,        String group        ArrayList<nestedgroup_CType> nestedgroup_ctypes    ) {
        this.name = name;
        this.b = b;
        this.group = group;
        this.nestedgroup_ctypes = nestedgroup_ctypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<nestedgroup_CType> getNestedgroup_ctypes() {
        return nestedgroup_ctypes;
    }

    public void addNestedgroup_ctype(Nestedgroup_ctype nestedgroup_ctype) {
        this.nestedgroup_ctypes.add(nestedgroup_ctype);
    }

}