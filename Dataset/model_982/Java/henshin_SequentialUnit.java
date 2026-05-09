





import java.util.List;
import java.util.ArrayList;

public class henshin_SequentialUnit extends TransformationUnit {

    private boolean rollback;
    private boolean strict;





    private List<henshin_TransformationUnit> henshin_transformationunits;


    public henshin_SequentialUnit(
        boolean rollback,        boolean strict    ) {
        super(
        );
        this.rollback = rollback;
        this.strict = strict;
        this.henshin_transformationunits = new ArrayList<>();
    }

    public henshin_SequentialUnit(
        boolean rollback,        boolean strict        ArrayList<henshin_TransformationUnit> henshin_transformationunits    ) {
        this.rollback = rollback;
        this.strict = strict;
        this.henshin_transformationunits = henshin_transformationunits;
    }

    public boolean getRollback() {
        return rollback;
    }

    public void setRollback(boolean rollback) {
        this.rollback = rollback;
    }
    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }

    public List<henshin_TransformationUnit> getHenshin_transformationunits() {
        return henshin_transformationunits;
    }

    public void addHenshin_transformationunit(Henshin_transformationunit henshin_transformationunit) {
        this.henshin_transformationunits.add(henshin_transformationunit);
    }

}