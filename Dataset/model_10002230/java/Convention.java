





import java.util.List;
import java.util.ArrayList;

public class Convention  {

    private int id_convention;
    private String numero;



    public Convention(
        int id_convention,        String numero    ) {
        this.id_convention = id_convention;
        this.numero = numero;
    }


    public int getId_convention() {
        return id_convention;
    }

    public void setId_convention(int id_convention) {
        this.id_convention = id_convention;
    }
    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }


}