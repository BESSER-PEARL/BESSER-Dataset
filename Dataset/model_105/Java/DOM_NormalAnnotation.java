





import java.util.List;
import java.util.ArrayList;

public class DOM_NormalAnnotation extends Annotation {






    private List<DOM_MemberValuePair> dom_membervaluepairs;


    public DOM_NormalAnnotation(
    ) {
        super(
        );
        this.dom_membervaluepairs = new ArrayList<>();
    }

    public DOM_NormalAnnotation(
        ArrayList<DOM_MemberValuePair> dom_membervaluepairs    ) {
        this.dom_membervaluepairs = dom_membervaluepairs;
    }


    public List<DOM_MemberValuePair> getDom_membervaluepairs() {
        return dom_membervaluepairs;
    }

    public void addDom_membervaluepair(Dom_membervaluepair dom_membervaluepair) {
        this.dom_membervaluepairs.add(dom_membervaluepair);
    }

}