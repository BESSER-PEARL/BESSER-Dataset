





import java.util.List;
import java.util.ArrayList;

public class fragdial_Component2 extends AbstractComponent {






    private fragdial_Component1 fragdial_component1;




    private List<fragdial_Component3> fragdial_component3s;


    public fragdial_Component2(
    ) {
        super(
        );
        this.fragdial_component3s = new ArrayList<>();
    }

    public fragdial_Component2(
        ArrayList<fragdial_Component3> fragdial_component3s    ) {
        this.fragdial_component3s = fragdial_component3s;
    }


    public fragdial_Component1 getFragdial_component1() {
        return fragdial_component1;
    }

    public void setFragdial_component1(fragdial_Component1 fragdial_component1) {
        this.fragdial_component1 = fragdial_component1;
    }
    public List<fragdial_Component3> getFragdial_component3s() {
        return fragdial_component3s;
    }

    public void addFragdial_component3(Fragdial_component3 fragdial_component3) {
        this.fragdial_component3s.add(fragdial_component3);
    }

}