





import java.util.List;
import java.util.ArrayList;

public class qm_TaggedElement extends QualityModelElement {






    private List<qm_Tag> qm_tags;


    public qm_TaggedElement(
    ) {
        super(
        );
        this.qm_tags = new ArrayList<>();
    }

    public qm_TaggedElement(
        ArrayList<qm_Tag> qm_tags    ) {
        this.qm_tags = qm_tags;
    }


    public List<qm_Tag> getQm_tags() {
        return qm_tags;
    }

    public void addQm_tag(Qm_tag qm_tag) {
        this.qm_tags.add(qm_tag);
    }

}