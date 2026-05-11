





import java.util.List;
import java.util.ArrayList;

public class arduino_Cabeca_Modificavel extends Acoes_Modificaveis {

    private int graus;



    public arduino_Cabeca_Modificavel(
        int graus    ) {
        super(
        );
        this.graus = graus;
    }


    public int getGraus() {
        return graus;
    }

    public void setGraus(int graus) {
        this.graus = graus;
    }


}