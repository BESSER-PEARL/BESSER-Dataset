





import java.util.List;
import java.util.ArrayList;

public class henshin_IndependentUnit extends TransformationUnit {






    private List<henshin_TransformationUnit> henshin_transformationunits;


    public henshin_IndependentUnit(
    ) {
        super(
        );
        this.henshin_transformationunits = new ArrayList<>();
    }

    public henshin_IndependentUnit(
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