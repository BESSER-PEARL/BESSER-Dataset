





import java.util.List;
import java.util.ArrayList;

public class ftp_VisualPort extends Port {






    private ftp_DigitalLamp ftp_digitallamp;




    private ftp_AnalogLamp ftp_analoglamp;


    public ftp_VisualPort(
    ) {
        super(
        );
    }



    public ftp_DigitalLamp getFtp_digitallamp() {
        return ftp_digitallamp;
    }

    public void setFtp_digitallamp(ftp_DigitalLamp ftp_digitallamp) {
        this.ftp_digitallamp = ftp_digitallamp;
    }
    public ftp_AnalogLamp getFtp_analoglamp() {
        return ftp_analoglamp;
    }

    public void setFtp_analoglamp(ftp_AnalogLamp ftp_analoglamp) {
        this.ftp_analoglamp = ftp_analoglamp;
    }

}