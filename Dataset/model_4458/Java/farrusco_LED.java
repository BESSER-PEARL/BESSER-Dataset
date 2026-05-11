





import java.util.List;
import java.util.ArrayList;

public class farrusco_LED extends Actuate {

    private String Nome;
    private String Ligado_ou_Desligado;



    public farrusco_LED(
        String Nome,        String Ligado_ou_Desligado    ) {
        super(
        );
        this.Nome = Nome;
        this.Ligado_ou_Desligado = Ligado_ou_Desligado;
    }


    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public String getLigado_ou_desligado() {
        return Ligado_ou_Desligado;
    }

    public void setLigado_ou_desligado(String Ligado_ou_Desligado) {
        this.Ligado_ou_Desligado = Ligado_ou_Desligado;
    }


}