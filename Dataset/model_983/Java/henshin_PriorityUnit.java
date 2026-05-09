





import java.util.List;
import java.util.ArrayList;

public class henshin_PriorityUnit extends TransformationUnit {






    private List<henshin_TransformationUnit> henshin_transformationunits;


    public henshin_PriorityUnit(
    ) {
        super(
        );
        this.henshin_transformationunits = new ArrayList<>();
    }

    public henshin_PriorityUnit(
        ArrayList<henshin_TransformationUnit> henshin_transformationunits    ) {
        this.henshin_transformationunits = henshin_transformationunits;
    }


    public List<henshin_TransformationUnit> getHenshin_transformationunits() {
        return henshin_transformationunits;
    }

    public void addHenshin_transformationunit(Henshin_transformationunit henshin_transformationunit) {
        this.henshin_transformationunits.add(henshin_transformationunit);
    }

}