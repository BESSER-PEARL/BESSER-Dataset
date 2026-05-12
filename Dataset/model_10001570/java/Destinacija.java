





import java.util.List;
import java.util.ArrayList;

public class Destinacija  {

    private int DestiID;
    private String DesDrzava;
    private String DesGrad;



    public Destinacija(
        int DestiID,        String DesDrzava,        String DesGrad    ) {
        this.DestiID = DestiID;
        this.DesDrzava = DesDrzava;
        this.DesGrad = DesGrad;
    }


    public int getDestiid() {
        return DestiID;
    }

    public void setDestiid(int DestiID) {
        this.DestiID = DestiID;
    }
    public String getDesdrzava() {
        return DesDrzava;
    }

    public void setDesdrzava(String DesDrzava) {
        this.DesDrzava = DesDrzava;
    }
    public String getDesgrad() {
        return DesGrad;
    }

    public void setDesgrad(String DesGrad) {
        this.DesGrad = DesGrad;
    }


}