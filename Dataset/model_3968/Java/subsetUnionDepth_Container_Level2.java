





import java.util.List;
import java.util.ArrayList;

public class subsetUnionDepth_Container_Level2 extends Container_Level1 {






    private List<subsetUnionDepth_Element_Level2> subsetuniondepth_element_level2s;


    public subsetUnionDepth_Container_Level2(
    ) {
        super(
        );
        this.subsetuniondepth_element_level2s = new ArrayList<>();
    }

    public subsetUnionDepth_Container_Level2(
        ArrayList<subsetUnionDepth_Element_Level2> subsetuniondepth_element_level2s    ) {
        this.subsetuniondepth_element_level2s = subsetuniondepth_element_level2s;
    }


    public List<subsetUnionDepth_Element_Level2> getSubsetuniondepth_element_level2s() {
        return subsetuniondepth_element_level2s;
    }

    public void addSubsetuniondepth_element_level2(Subsetuniondepth_element_level2 subsetuniondepth_element_level2) {
        this.subsetuniondepth_element_level2s.add(subsetuniondepth_element_level2);
    }

}