





import java.util.List;
import java.util.ArrayList;

public class conta_Poupan_a  {

    private int tempo;
    private float juros;



    public conta_Poupan_a(
        int tempo,        float juros    ) {
        this.tempo = tempo;
        this.juros = juros;
    }


    public int getTempo() {
        return tempo;
    }

    public void setTempo(int tempo) {
        this.tempo = tempo;
    }
    public float getJuros() {
        return juros;
    }

    public void setJuros(float juros) {
        this.juros = juros;
    }


}