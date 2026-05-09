





import java.util.List;
import java.util.ArrayList;

public class henshin_CountedUnit extends TransformationUnit {

    private int count;





    private henshin_TransformationUnit henshin_transformationunit;


    public henshin_CountedUnit(
        int count    ) {
        super(
        );
        this.count = count;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public henshin_TransformationUnit getHenshin_transformationunit() {
        return henshin_transformationunit;
    }

    public void setHenshin_transformationunit(henshin_TransformationUnit henshin_transformationunit) {
        this.henshin_transformationunit = henshin_transformationunit;
    }

}