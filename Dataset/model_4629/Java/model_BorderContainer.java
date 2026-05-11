





import java.util.List;
import java.util.ArrayList;

public class model_BorderContainer extends Container {

    private int horizontalSpacing;
    private int verticalSpacing;





    private List<model_BorderChild> model_borderchilds;


    public model_BorderContainer(
        int horizontalSpacing,        int verticalSpacing    ) {
        super(
        );
        this.horizontalSpacing = horizontalSpacing;
        this.verticalSpacing = verticalSpacing;
        this.model_borderchilds = new ArrayList<>();
    }

    public model_BorderContainer(
        int horizontalSpacing,        int verticalSpacing        ArrayList<model_BorderChild> model_borderchilds    ) {
        this.horizontalSpacing = horizontalSpacing;
        this.verticalSpacing = verticalSpacing;
        this.model_borderchilds = model_borderchilds;
    }

    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }
    public int getVerticalspacing() {
        return verticalSpacing;
    }

    public void setVerticalspacing(int verticalSpacing) {
        this.verticalSpacing = verticalSpacing;
    }

    public List<model_BorderChild> getModel_borderchilds() {
        return model_borderchilds;
    }

    public void addModel_borderchild(Model_borderchild model_borderchild) {
        this.model_borderchilds.add(model_borderchild);
    }

}