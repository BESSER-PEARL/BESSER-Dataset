





import java.util.List;
import java.util.ArrayList;

public class Korvauksen_maksaminen_UseCase  {






    private Vakuutusyhti__Actor vakuutusyhti__actor;




    private K_ytt_j__Actor k_ytt_j__actor;


    public Korvauksen_maksaminen_UseCase(
    ) {
    }



    public Vakuutusyhti__Actor getVakuutusyhti__actor() {
        return vakuutusyhti__actor;
    }

    public void setVakuutusyhti__actor(Vakuutusyhti__Actor vakuutusyhti__actor) {
        this.vakuutusyhti__actor = vakuutusyhti__actor;
    }
    public K_ytt_j__Actor getK_ytt_j__actor() {
        return k_ytt_j__actor;
    }

    public void setK_ytt_j__actor(K_ytt_j__Actor k_ytt_j__actor) {
        this.k_ytt_j__actor = k_ytt_j__actor;
    }

}