





import java.util.List;
import java.util.ArrayList;

public class login_UseCase  {






    private pengunjung_Actor pengunjung_actor;




    private pemilik_yayasan_Actor pemilik_yayasan_actor;




    private pengurus_yayasan_Actor pengurus_yayasan_actor;


    public login_UseCase(
    ) {
    }



    public pengunjung_Actor getPengunjung_actor() {
        return pengunjung_actor;
    }

    public void setPengunjung_actor(pengunjung_Actor pengunjung_actor) {
        this.pengunjung_actor = pengunjung_actor;
    }
    public pemilik_yayasan_Actor getPemilik_yayasan_actor() {
        return pemilik_yayasan_actor;
    }

    public void setPemilik_yayasan_actor(pemilik_yayasan_Actor pemilik_yayasan_actor) {
        this.pemilik_yayasan_actor = pemilik_yayasan_actor;
    }
    public pengurus_yayasan_Actor getPengurus_yayasan_actor() {
        return pengurus_yayasan_actor;
    }

    public void setPengurus_yayasan_actor(pengurus_yayasan_Actor pengurus_yayasan_actor) {
        this.pengurus_yayasan_actor = pengurus_yayasan_actor;
    }

}