





import java.util.List;
import java.util.ArrayList;

public class presentation_SoundType  {

    private String actuate;
    private String playFull;
    private String href;
    private String show;
    private String type;



    public presentation_SoundType(
        String actuate,        String playFull,        String href,        String show,        String type    ) {
        this.actuate = actuate;
        this.playFull = playFull;
        this.href = href;
        this.show = show;
        this.type = type;
    }


    public String getActuate() {
        return actuate;
    }

    public void setActuate(String actuate) {
        this.actuate = actuate;
    }
    public String getPlayfull() {
        return playFull;
    }

    public void setPlayfull(String playFull) {
        this.playFull = playFull;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getShow() {
        return show;
    }

    public void setShow(String show) {
        this.show = show;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}