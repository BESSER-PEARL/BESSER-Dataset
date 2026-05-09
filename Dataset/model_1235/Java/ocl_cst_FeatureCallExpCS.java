





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_FeatureCallExpCS extends CallExpCS {






    private PathNameCS pathnamecs;




    private IsMarkedPreCS ismarkedprecs;




    private List<OCLExpressionCS> oclexpressioncss;


    public ocl_cst_FeatureCallExpCS(
    ) {
        super(
        );
        this.oclexpressioncss = new ArrayList<>();
    }

    public ocl_cst_FeatureCallExpCS(
        ArrayList<OCLExpressionCS> oclexpressioncss    ) {
        this.oclexpressioncss = oclexpressioncss;
    }


    public PathNameCS getPathnamecs() {
        return pathnamecs;
    }

    public void setPathnamecs(PathNameCS pathnamecs) {
        this.pathnamecs = pathnamecs;
    }
    public IsMarkedPreCS getIsmarkedprecs() {
        return ismarkedprecs;
    }

    public void setIsmarkedprecs(IsMarkedPreCS ismarkedprecs) {
        this.ismarkedprecs = ismarkedprecs;
    }
    public List<OCLExpressionCS> getOclexpressioncss() {
        return oclexpressioncss;
    }

    public void addOclexpressioncs(Oclexpressioncs oclexpressioncs) {
        this.oclexpressioncss.add(oclexpressioncs);
    }

}