





import java.util.List;
import java.util.ArrayList;

public class arduino_Corpo extends Acoes_Predefinidas {

    private boolean evitarObstaculo;



    public arduino_Corpo(
        boolean evitarObstaculo    ) {
        super(
        );
        this.evitarObstaculo = evitarObstaculo;
    }


    public boolean getEvitarobstaculo() {
        return evitarObstaculo;
    }

    public void setEvitarobstaculo(boolean evitarObstaculo) {
        this.evitarObstaculo = evitarObstaculo;
    }


}