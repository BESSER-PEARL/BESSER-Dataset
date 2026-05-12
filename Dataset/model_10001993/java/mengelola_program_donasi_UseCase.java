





import java.util.List;
import java.util.ArrayList;

public class mengelola_program_donasi_UseCase  {






    private pengunjung_Actor pengunjung_actor;




    private pengurus_yayasan_Actor pengurus_yayasan_actor;


    public mengelola_program_donasi_UseCase(
    ) {
    }



    public pengunjung_Actor getPengunjung_actor() {
        return pengunjung_actor;
    }

    public void setPengunjung_actor(pengunjung_Actor pengunjung_actor) {
        this.pengunjung_actor = pengunjung_actor;
    }
    public pengurus_yayasan_Actor getPengurus_yayasan_actor() {
        return pengurus_yayasan_actor;
    }

    public void setPengurus_yayasan_actor(pengurus_yayasan_Actor pengurus_yayasan_actor) {
        this.pengurus_yayasan_actor = pengurus_yayasan_actor;
    }

}