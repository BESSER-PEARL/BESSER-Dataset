





import java.util.List;
import java.util.ArrayList;

public class compartments_ChildOfB_F  {

    private String name;





    private compartments_TopNodeB compartments_topnodeb;




    private compartments_ChildOfA_D compartments_childofa_d;


    public compartments_ChildOfB_F(
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
    public compartments_ChildOfA_D getCompartments_childofa_d() {
        return compartments_childofa_d;
    }

    public void setCompartments_childofa_d(compartments_ChildOfA_D compartments_childofa_d) {
        this.compartments_childofa_d = compartments_childofa_d;
    }

}