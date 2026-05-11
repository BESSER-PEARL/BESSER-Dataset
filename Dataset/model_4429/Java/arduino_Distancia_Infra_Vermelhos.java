





import java.util.List;
import java.util.ArrayList;

public class arduino_Distancia_Infra_Vermelhos extends Condicao {

    private int distancia;



    public arduino_Distancia_Infra_Vermelhos(
        int distancia    ) {
        super(
        );
        this.distancia = distancia;
    }


    public int getDistancia() {
        return distancia;
    }

    public void setDistancia(int distancia) {
        this.distancia = distancia;
    }


}