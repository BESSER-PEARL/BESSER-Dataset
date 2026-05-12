





import java.util.List;
import java.util.ArrayList;

public class Smart_mirror  {

    private boolean PhoneConnect;
    private boolean Status;
    private None Display_newsfeed;
    private float Update;
    private None security;



    public Smart_mirror(
        boolean PhoneConnect,        boolean Status,        None Display_newsfeed,        float Update,        None security    ) {
        this.PhoneConnect = PhoneConnect;
        this.Status = Status;
        this.Display_newsfeed = Display_newsfeed;
        this.Update = Update;
        this.security = security;
    }


    public boolean getPhoneconnect() {
        return PhoneConnect;
    }

    public void setPhoneconnect(boolean PhoneConnect) {
        this.PhoneConnect = PhoneConnect;
    }
    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }
    public None getDisplay_newsfeed() {
        return Display_newsfeed;
    }

    public void setDisplay_newsfeed(None Display_newsfeed) {
        this.Display_newsfeed = Display_newsfeed;
    }
    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }
    public None getSecurity() {
        return security;
    }

    public void setSecurity(None security) {
        this.security = security;
    }


}