





import java.util.List;
import java.util.ArrayList;

public class TransitionQVT_A extends Element {

    private String reduction;
    private float height;



    public TransitionQVT_A(
        String reduction,        float height    ) {
        super(
        );
        this.reduction = reduction;
        this.height = height;
    }


    public String getReduction() {
        return reduction;
    }

    public void setReduction(String reduction) {
        this.reduction = reduction;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }


}