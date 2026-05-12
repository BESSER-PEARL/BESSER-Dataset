





import java.util.List;
import java.util.ArrayList;

public class Putovanje  {

    private String Grad;
    private String Dr_ava;
    private int PutovID;



    public Putovanje(
        String Grad,        String Dr_ava,        int PutovID    ) {
        this.Grad = Grad;
        this.Dr_ava = Dr_ava;
        this.PutovID = PutovID;
    }


    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }
    public String getDr_ava() {
        return Dr_ava;
    }

    public void setDr_ava(String Dr_ava) {
        this.Dr_ava = Dr_ava;
    }
    public int getPutovid() {
        return PutovID;
    }

    public void setPutovid(int PutovID) {
        this.PutovID = PutovID;
    }


}