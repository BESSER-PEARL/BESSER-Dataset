





import java.util.List;
import java.util.ArrayList;

public class henshin_IteratedUnit extends TransformationUnit {

    private String iterations;





    private henshin_TransformationUnit henshin_transformationunit;


    public henshin_IteratedUnit(
        String iterations    ) {
        super(
        );
        this.iterations = iterations;
    }


    public String getIterations() {
        return iterations;
    }

    public void setIterations(String iterations) {
        this.iterations = iterations;
    }

    public henshin_TransformationUnit getHenshin_transformationunit() {
        return henshin_transformationunit;
    }

    public void setHenshin_transformationunit(henshin_TransformationUnit henshin_transformationunit) {
        this.henshin_transformationunit = henshin_transformationunit;
    }

}