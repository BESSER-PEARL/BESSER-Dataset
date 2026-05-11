





import java.util.List;
import java.util.ArrayList;

public class farrusco_Distancia extends Condition {

    private boolean how_sucess;
    private int distancia;



    public farrusco_Distancia(
        boolean how_sucess,        int distancia    ) {
        super(
        );
        this.how_sucess = how_sucess;
        this.distancia = distancia;
    }


    public boolean getHow_sucess() {
        return how_sucess;
    }

    public void setHow_sucess(boolean how_sucess) {
        this.how_sucess = how_sucess;
    }
    public int getDistancia() {
        return distancia;
    }

    public void setDistancia(int distancia) {
        this.distancia = distancia;
    }


}