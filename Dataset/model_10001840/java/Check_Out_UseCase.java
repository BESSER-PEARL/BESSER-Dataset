





import java.util.List;
import java.util.ArrayList;

public class Check_Out_UseCase  {






    private Pemesan_Actor pemesan_actor;




    private Pengunjung_Actor pengunjung_actor;


    public Check_Out_UseCase(
    ) {
    }



    public Pemesan_Actor getPemesan_actor() {
        return pemesan_actor;
    }

    public void setPemesan_actor(Pemesan_Actor pemesan_actor) {
        this.pemesan_actor = pemesan_actor;
    }
    public Pengunjung_Actor getPengunjung_actor() {
        return pengunjung_actor;
    }

    public void setPengunjung_actor(Pengunjung_Actor pengunjung_actor) {
        this.pengunjung_actor = pengunjung_actor;
    }

}