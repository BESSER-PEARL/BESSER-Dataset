





import java.util.List;
import java.util.ArrayList;

public class model_Anchor extends Feature {

    private int max;
    private String direction;





    private model_EReference model_ereference;


    public model_Anchor(
        int max,        String direction    ) {
        super(
        );
        this.max = max;
        this.direction = direction;
    }


    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public model_EReference getModel_ereference() {
        return model_ereference;
    }

    public void setModel_ereference(model_EReference model_ereference) {
        this.model_ereference = model_ereference;
    }

}