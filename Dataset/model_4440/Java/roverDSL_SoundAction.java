





import java.util.List;
import java.util.ArrayList;

public class roverDSL_SoundAction extends Action {

    private String sound;



    public roverDSL_SoundAction(
        String sound    ) {
        super(
        );
        this.sound = sound;
    }


    public String getSound() {
        return sound;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }


}