





import java.util.List;
import java.util.ArrayList;

public class farrusco_Espera extends Condition {

    private String Nome;
    private int Tempo;



    public farrusco_Espera(
        String Nome,        int Tempo    ) {
        super(
        );
        this.Nome = Nome;
        this.Tempo = Tempo;
    }


    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public int getTempo() {
        return Tempo;
    }

    public void setTempo(int Tempo) {
        this.Tempo = Tempo;
    }


}