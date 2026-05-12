





import java.util.List;
import java.util.ArrayList;

public class login_UseCase2  {






    private pemilik_yayasan_Actor pemilik_yayasan_actor;




    private pengurus_yayasan_Actor pengurus_yayasan_actor;


    public login_UseCase2(
    ) {
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