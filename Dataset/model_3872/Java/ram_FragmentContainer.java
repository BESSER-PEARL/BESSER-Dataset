





import java.util.List;
import java.util.ArrayList;

public class ram_FragmentContainer  {






    private ram_InteractionFragment ram_interactionfragment;




    private List<ram_InteractionFragment> ram_interactionfragments;


    public ram_FragmentContainer(
    ) {
        this.ram_interactionfragments = new ArrayList<>();
    }

    public ram_FragmentContainer(
        ArrayList<ram_InteractionFragment> ram_interactionfragments    ) {
        this.ram_interactionfragments = ram_interactionfragments;
    }


    public ram_InteractionFragment getRam_interactionfragment() {
        return ram_interactionfragment;
    }

    public void setRam_interactionfragment(ram_InteractionFragment ram_interactionfragment) {
        this.ram_interactionfragment = ram_interactionfragment;
    }
    public List<ram_InteractionFragment> getRam_interactionfragments() {
        return ram_interactionfragments;
    }

    public void addRam_interactionfragment(Ram_interactionfragment ram_interactionfragment) {
        this.ram_interactionfragments.add(ram_interactionfragment);
    }

}