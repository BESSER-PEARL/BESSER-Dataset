





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_Fragments  {






    private List<Fragment> fragments;


    public aggregator_p2view_Fragments(
    ) {
        this.fragments = new ArrayList<>();
    }

    public aggregator_p2view_Fragments(
        ArrayList<Fragment> fragments    ) {
        this.fragments = fragments;
    }


    public List<Fragment> getFragments() {
        return fragments;
    }

    public void addFragment(Fragment fragment) {
        this.fragments.add(fragment);
    }

}