





import java.util.List;
import java.util.ArrayList;

public class network_UserRegistration  {

    private int serialVersionUID;
    private String SAVE_DIR;



    public network_UserRegistration(
        int serialVersionUID,        String SAVE_DIR    ) {
        this.serialVersionUID = serialVersionUID;
        this.SAVE_DIR = SAVE_DIR;
    }


    public int getSerialversionuid() {
        return serialVersionUID;
    }

    public void setSerialversionuid(int serialVersionUID) {
        this.serialVersionUID = serialVersionUID;
    }
    public String getSave_dir() {
        return SAVE_DIR;
    }

    public void setSave_dir(String SAVE_DIR) {
        this.SAVE_DIR = SAVE_DIR;
    }


}