





import java.util.List;
import java.util.ArrayList;

public class Destinacija  {

    private int DestiID;
    private String DesGrad;
    private String DesDrzava;



    public Destinacija(
        int DestiID,        String DesGrad,        String DesDrzava    ) {
        this.DestiID = DestiID;
        this.DesGrad = DesGrad;
        this.DesDrzava = DesDrzava;
    }


    public int getDestiid() {
        return DestiID;
    }

    public void setDestiid(int DestiID) {
        this.DestiID = DestiID;
    }
    public String getDesgrad() {
        return DesGrad;
    }

    public void setDesgrad(String DesGrad) {
        this.DesGrad = DesGrad;
    }
    public String getDesdrzava() {
        return DesDrzava;
    }

    public void setDesdrzava(String DesDrzava) {
        this.DesDrzava = DesDrzava;
    }


}