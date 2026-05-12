




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Pago  {

    private float PSI;
    private LocalDate Contra_entrega;



    public Pago(
        float PSI,        LocalDate Contra_entrega    ) {
        this.PSI = PSI;
        this.Contra_entrega = Contra_entrega;
    }


    public float getPsi() {
        return PSI;
    }

    public void setPsi(float PSI) {
        this.PSI = PSI;
    }
    public LocalDate getContra_entrega() {
        return Contra_entrega;
    }

    public void setContra_entrega(LocalDate Contra_entrega) {
        this.Contra_entrega = Contra_entrega;
    }


}