





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Ressource extends ProcessElement {

    private int count;
    private String name;





    private simplepdl_Allocation simplepdl_allocation;


    public simplepdl_Ressource(
        int count,        String name    ) {
        super(
        );
        this.count = count;
        this.name = name;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplepdl_Allocation getSimplepdl_allocation() {
        return simplepdl_allocation;
    }

    public void setSimplepdl_allocation(simplepdl_Allocation simplepdl_allocation) {
        this.simplepdl_allocation = simplepdl_allocation;
    }

}