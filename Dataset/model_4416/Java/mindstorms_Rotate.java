





import java.util.List;
import java.util.ArrayList;

public class mindstorms_Rotate extends Action {

    private int degrees;
    private boolean random;



    public mindstorms_Rotate(
        int degrees,        boolean random    ) {
        super(
        );
        this.degrees = degrees;
        this.random = random;
    }


    public int getDegrees() {
        return degrees;
    }

    public void setDegrees(int degrees) {
        this.degrees = degrees;
    }
    public boolean getRandom() {
        return random;
    }

    public void setRandom(boolean random) {
        this.random = random;
    }


}