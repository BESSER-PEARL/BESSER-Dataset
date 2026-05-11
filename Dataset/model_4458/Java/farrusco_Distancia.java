





import java.util.List;
import java.util.ArrayList;

public class farrusco_Distancia extends Condition {

    private String Menor_Maior;
    private int distancia;
    private String Nome;



    public farrusco_Distancia(
        String Menor_Maior,        int distancia,        String Nome    ) {
        super(
        );
        this.Menor_Maior = Menor_Maior;
        this.distancia = distancia;
        this.Nome = Nome;
    }


    public String getMenor_maior() {
        return Menor_Maior;
    }

    public void setMenor_maior(String Menor_Maior) {
        this.Menor_Maior = Menor_Maior;
    }
    public int getDistancia() {
        return distancia;
    }

    public void setDistancia(int distancia) {
        this.distancia = distancia;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }


}