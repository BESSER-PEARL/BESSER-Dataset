





import java.util.List;
import java.util.ArrayList;

public class documentation_FragmentContainer extends TextContainer {






    private List<documentation_Fragment> documentation_fragments;


    public documentation_FragmentContainer(
    ) {
        super(
        );
        this.documentation_fragments = new ArrayList<>();
    }

    public documentation_FragmentContainer(
        ArrayList<documentation_Fragment> documentation_fragments    ) {
        this.documentation_fragments = documentation_fragments;
    }


    public List<documentation_Fragment> getDocumentation_fragments() {
        return documentation_fragments;
    }

    public void addDocumentation_fragment(Documentation_fragment documentation_fragment) {
        this.documentation_fragments.add(documentation_fragment);
    }

}