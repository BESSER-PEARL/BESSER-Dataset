





import java.util.List;
import java.util.ArrayList;

public class HomeTheatre  {

    private String HTID;





    private TV tv;




    private Radio radio;


    public HomeTheatre(
        String HTID    ) {
        this.HTID = HTID;
    }


    public String getHtid() {
        return HTID;
    }

    public void setHtid(String HTID) {
        this.HTID = HTID;
    }

    public TV getTv() {
        return tv;
    }

    public void setTv(TV tv) {
        this.tv = tv;
    }
    public Radio getRadio() {
        return radio;
    }

    public void setRadio(Radio radio) {
        this.radio = radio;
    }

}