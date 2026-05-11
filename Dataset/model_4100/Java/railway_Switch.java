





import java.util.List;
import java.util.ArrayList;

public class railway_Switch extends TrackElement {

    private String currentPosition;



    public railway_Switch(
        String currentPosition    ) {
        super(
        );
        this.currentPosition = currentPosition;
    }


    public String getCurrentposition() {
        return currentPosition;
    }

    public void setCurrentposition(String currentPosition) {
        this.currentPosition = currentPosition;
    }


}