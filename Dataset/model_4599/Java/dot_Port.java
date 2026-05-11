





import java.util.List;
import java.util.ArrayList;

public class dot_Port extends Commentable, Identifiable {

    private String compass;



    public dot_Port(
        String compass    ) {
        super(
        );
        this.compass = compass;
    }


    public String getCompass() {
        return compass;
    }

    public void setCompass(String compass) {
        this.compass = compass;
    }


}