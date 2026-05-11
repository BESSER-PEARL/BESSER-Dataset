





import java.util.List;
import java.util.ArrayList;

public class compartments_ChildOfB_E  {

    private String name;





    private compartments_TopNodeB compartments_topnodeb;




    private compartments_ChildOfA_C compartments_childofa_c;


    public compartments_ChildOfB_E(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public compartments_TopNodeB getCompartments_topnodeb() {
        return compartments_topnodeb;
    }

    public void setCompartments_topnodeb(compartments_TopNodeB compartments_topnodeb) {
        this.compartments_topnodeb = compartments_topnodeb;
    }
    public compartments_ChildOfA_C getCompartments_childofa_c() {
        return compartments_childofa_c;
    }

    public void setCompartments_childofa_c(compartments_ChildOfA_C compartments_childofa_c) {
        this.compartments_childofa_c = compartments_childofa_c;
    }

}