





import java.util.List;
import java.util.ArrayList;

public class Gateway  {

    private float Update;
    private None WebPLC_configure;
    private None Status;



    public Gateway(
        float Update,        None WebPLC_configure,        None Status    ) {
        this.Update = Update;
        this.WebPLC_configure = WebPLC_configure;
        this.Status = Status;
    }


    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }
    public None getWebplc_configure() {
        return WebPLC_configure;
    }

    public void setWebplc_configure(None WebPLC_configure) {
        this.WebPLC_configure = WebPLC_configure;
    }
    public None getStatus() {
        return Status;
    }

    public void setStatus(None Status) {
        this.Status = Status;
    }


}