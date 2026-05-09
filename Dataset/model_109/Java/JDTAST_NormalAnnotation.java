





import java.util.List;
import java.util.ArrayList;

public class JDTAST_NormalAnnotation extends Annotation {






    private List<JDTAST_MemberValuePair> jdtast_membervaluepairs;


    public JDTAST_NormalAnnotation(
    ) {
        super(
        );
        this.jdtast_membervaluepairs = new ArrayList<>();
    }

    public JDTAST_NormalAnnotation(
        ArrayList<JDTAST_MemberValuePair> jdtast_membervaluepairs    ) {
        this.jdtast_membervaluepairs = jdtast_membervaluepairs;
    }


    public List<JDTAST_MemberValuePair> getJdtast_membervaluepairs() {
        return jdtast_membervaluepairs;
    }

    public void addJdtast_membervaluepair(Jdtast_membervaluepair jdtast_membervaluepair) {
        this.jdtast_membervaluepairs.add(jdtast_membervaluepair);
    }

}