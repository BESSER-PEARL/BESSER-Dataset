





import java.util.List;
import java.util.ArrayList;

public class tracker_Swine extends Animal {

    private int leftEarNotching;
    private int rightEarNotching;
    private String swineBreed;



    public tracker_Swine(
        int leftEarNotching,        int rightEarNotching,        String swineBreed    ) {
        super(
        );
        this.leftEarNotching = leftEarNotching;
        this.rightEarNotching = rightEarNotching;
        this.swineBreed = swineBreed;
    }


    public int getLeftearnotching() {
        return leftEarNotching;
    }

    public void setLeftearnotching(int leftEarNotching) {
        this.leftEarNotching = leftEarNotching;
    }
    public int getRightearnotching() {
        return rightEarNotching;
    }

    public void setRightearnotching(int rightEarNotching) {
        this.rightEarNotching = rightEarNotching;
    }
    public String getSwinebreed() {
        return swineBreed;
    }

    public void setSwinebreed(String swineBreed) {
        this.swineBreed = swineBreed;
    }


}