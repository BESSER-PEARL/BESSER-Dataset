





import java.util.List;
import java.util.ArrayList;

public class farrusco_IRdist extends Condition {

    private int distancia;
    private boolean how_sucess;



    public farrusco_IRdist(
        int distancia,        boolean how_sucess    ) {
        super(
        );
        this.distancia = distancia;
        this.how_sucess = how_sucess;
    }


    public int getDistancia() {
        return distancia;
    }

    public void setDistancia(int distancia) {
        this.distancia = distancia;
    }
    public boolean getHow_sucess() {
        return how_sucess;
    }

    public void setHow_sucess(boolean how_sucess) {
        this.how_sucess = how_sucess;
    }


}