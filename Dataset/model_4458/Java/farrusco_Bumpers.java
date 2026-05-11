





import java.util.List;
import java.util.ArrayList;

public class farrusco_Bumpers extends Condition {

    private String Bumper_Esquerdo_ou_Direito;
    private String Nome;



    public farrusco_Bumpers(
        String Bumper_Esquerdo_ou_Direito,        String Nome    ) {
        super(
        );
        this.Bumper_Esquerdo_ou_Direito = Bumper_Esquerdo_ou_Direito;
        this.Nome = Nome;
    }


    public String getBumper_esquerdo_ou_direito() {
        return Bumper_Esquerdo_ou_Direito;
    }

    public void setBumper_esquerdo_ou_direito(String Bumper_Esquerdo_ou_Direito) {
        this.Bumper_Esquerdo_ou_Direito = Bumper_Esquerdo_ou_Direito;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }


}