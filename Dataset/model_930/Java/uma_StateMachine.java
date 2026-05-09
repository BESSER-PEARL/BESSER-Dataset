





import java.util.List;
import java.util.ArrayList;

public class uma_StateMachine extends WorkDefinition {






    private uma_Region uma_region;




    private List<uma_Region> uma_regions;




    private uma_State uma_state;


    public uma_StateMachine(
    ) {
        super(
        );
        this.uma_regions = new ArrayList<>();
    }

    public uma_StateMachine(
        ArrayList<uma_Region> uma_regions    ) {
        this.uma_regions = uma_regions;
    }


    public uma_Region getUma_region() {
        return uma_region;
    }

    public void setUma_region(uma_Region uma_region) {
        this.uma_region = uma_region;
    }
    public List<uma_Region> getUma_regions() {
        return uma_regions;
    }

    public void addUma_region(Uma_region uma_region) {
        this.uma_regions.add(uma_region);
    }
    public uma_State getUma_state() {
        return uma_state;
    }

    public void setUma_state(uma_State uma_state) {
        this.uma_state = uma_state;
    }

}