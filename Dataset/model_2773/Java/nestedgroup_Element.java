





import java.util.List;
import java.util.ArrayList;

public class nestedgroup_Element  {

    private String name;
    private String true;
    private String mixed;





    private nestedgroup_Element nestedgroup_element;




    private List<nestedgroup_CType> nestedgroup_ctypes;


    public nestedgroup_Element(
        String name,        String true,        String mixed    ) {
        this.name = name;
        this.true = true;
        this.mixed = mixed;
        this.nestedgroup_ctypes = new ArrayList<>();
    }

    public nestedgroup_Element(
        String name,        String true,        String mixed        ArrayList<nestedgroup_CType> nestedgroup_ctypes    ) {
        this.name = name;
        this.true = true;
        this.mixed = mixed;
        this.nestedgroup_ctypes = nestedgroup_ctypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrue() {
        return true;
    }

    public void setTrue(String true) {
        this.true = true;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public nestedgroup_Element getNestedgroup_element() {
        return nestedgroup_element;
    }

    public void setNestedgroup_element(nestedgroup_Element nestedgroup_element) {
        this.nestedgroup_element = nestedgroup_element;
    }
    public List<nestedgroup_CType> getNestedgroup_ctypes() {
        return nestedgroup_ctypes;
    }

    public void addNestedgroup_ctype(Nestedgroup_ctype nestedgroup_ctype) {
        this.nestedgroup_ctypes.add(nestedgroup_ctype);
    }

}