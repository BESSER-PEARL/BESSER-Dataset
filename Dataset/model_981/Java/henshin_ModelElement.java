





import java.util.List;
import java.util.ArrayList;

public class henshin_ModelElement  {






    private List<henshin_Annotation> henshin_annotations;


    public henshin_ModelElement(
    ) {
        this.henshin_annotations = new ArrayList<>();
    }

    public henshin_ModelElement(
        ArrayList<henshin_Annotation> henshin_annotations    ) {
        this.henshin_annotations = henshin_annotations;
    }


    public List<henshin_Annotation> getHenshin_annotations() {
        return henshin_annotations;
    }

    public void addHenshin_annotation(Henshin_annotation henshin_annotation) {
        this.henshin_annotations.add(henshin_annotation);
    }

}