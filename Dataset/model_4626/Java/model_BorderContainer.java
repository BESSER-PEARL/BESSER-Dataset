





import java.util.List;
import java.util.ArrayList;

public class model_BorderContainer extends Container {

    private int horizontalSpacing;
    private int verticalSpacing;



    public model_BorderContainer(
        int horizontalSpacing,        int verticalSpacing    ) {
        super(
        );
        this.horizontalSpacing = horizontalSpacing;
        this.verticalSpacing = verticalSpacing;
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


}