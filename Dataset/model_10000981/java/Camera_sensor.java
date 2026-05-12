





import java.util.List;
import java.util.ArrayList;

public class Camera_sensor  {

    private int Image_ID;
    private int Video_ID;





    private Door_Security door_security;


    public Camera_sensor(
        int Image_ID,        int Video_ID    ) {
        this.Image_ID = Image_ID;
        this.Video_ID = Video_ID;
    }


    public int getImage_id() {
        return Image_ID;
    }

    public void setImage_id(int Image_ID) {
        this.Image_ID = Image_ID;
    }
    public int getVideo_id() {
        return Video_ID;
    }

    public void setVideo_id(int Video_ID) {
        this.Video_ID = Video_ID;
    }

    public Door_Security getDoor_security() {
        return door_security;
    }

    public void setDoor_security(Door_Security door_security) {
        this.door_security = door_security;
    }

}