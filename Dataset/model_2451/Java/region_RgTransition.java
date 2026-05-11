





import java.util.List;
import java.util.ArrayList;

public class region_RgTransition extends Referenced {

    private String event;
    private String message;
    private String effect;





    private region_RgState region_rgstate;




    private region_RgInitialPseudostate region_rginitialpseudostate;




    private region_RgState region_rgstate;


    public region_RgTransition(
        String event,        String message,        String effect    ) {
        super(
        );
        this.event = event;
        this.message = message;
        this.effect = effect;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }

    public region_RgState getRegion_rgstate() {
        return region_rgstate;
    }

    public void setRegion_rgstate(region_RgState region_rgstate) {
        this.region_rgstate = region_rgstate;
    }
    public region_RgInitialPseudostate getRegion_rginitialpseudostate() {
        return region_rginitialpseudostate;
    }

    public void setRegion_rginitialpseudostate(region_RgInitialPseudostate region_rginitialpseudostate) {
        this.region_rginitialpseudostate = region_rginitialpseudostate;
    }
    public region_RgState getRegion_rgstate() {
        return region_rgstate;
    }

    public void setRegion_rgstate(region_RgState region_rgstate) {
        this.region_rgstate = region_rgstate;
    }

}