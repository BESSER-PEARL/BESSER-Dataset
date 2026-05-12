





import java.util.List;
import java.util.ArrayList;

public class build_Feature extends InstallationUnit {

    private boolean inProduct;





    private build_Contribution build_contribution;




    private List<build_Category> build_categorys;




    private build_Category build_category;


    public build_Feature(
        boolean inProduct    ) {
        super(
        );
        this.inProduct = inProduct;
        this.build_categorys = new ArrayList<>();
    }

    public build_Feature(
        boolean inProduct        ArrayList<build_Category> build_categorys    ) {
        this.inProduct = inProduct;
        this.build_categorys = build_categorys;
    }

    public boolean getInproduct() {
        return inProduct;
    }

    public void setInproduct(boolean inProduct) {
        this.inProduct = inProduct;
    }

    public build_Contribution getBuild_contribution() {
        return build_contribution;
    }

    public void setBuild_contribution(build_Contribution build_contribution) {
        this.build_contribution = build_contribution;
    }
    public List<build_Category> getBuild_categorys() {
        return build_categorys;
    }

    public void addBuild_category(Build_category build_category) {
        this.build_categorys.add(build_category);
    }
    public build_Category getBuild_category() {
        return build_category;
    }

    public void setBuild_category(build_Category build_category) {
        this.build_category = build_category;
    }

}