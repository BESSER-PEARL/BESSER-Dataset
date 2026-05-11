





import java.util.List;
import java.util.ArrayList;

public class arduino_Corpo_Modificavel extends Acoes_Modificaveis {

    private int tempo;
    private boolean evitarObstaculo;



    public arduino_Corpo_Modificavel(
        int tempo,        boolean evitarObstaculo    ) {
        super(
        );
        this.tempo = tempo;
        this.evitarObstaculo = evitarObstaculo;
    }


    public int getTempo() {
        return tempo;
    }

    public void setTempo(int tempo) {
        this.tempo = tempo;
    }
    public boolean getEvitarobstaculo() {
        return evitarObstaculo;
    }

    public void setEvitarobstaculo(boolean evitarObstaculo) {
        this.evitarObstaculo = evitarObstaculo;
    }


}