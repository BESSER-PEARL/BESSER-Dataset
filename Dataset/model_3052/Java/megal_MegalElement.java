





import java.util.List;
import java.util.ArrayList;

public class megal_MegalElement  {






    private List<megal_MegalAnnotation> megal_megalannotations;


    public megal_MegalElement(
    ) {
        this.megal_megalannotations = new ArrayList<>();
    }

    public megal_MegalElement(
        ArrayList<megal_MegalAnnotation> megal_megalannotations    ) {
        this.megal_megalannotations = megal_megalannotations;
    }


    public List<megal_MegalAnnotation> getMegal_megalannotations() {
        return megal_megalannotations;
    }

    public void addMegal_megalannotation(Megal_megalannotation megal_megalannotation) {
        this.megal_megalannotations.add(megal_megalannotation);
    }

}