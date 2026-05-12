





import java.util.List;
import java.util.ArrayList;

public class Package2_login_UseCase  {






    private Package2_Pengurus_Yayasan_Actor package2_pengurus_yayasan_actor;




    private Package2_Donatur_Actor package2_donatur_actor;


    public Package2_login_UseCase(
    ) {
    }



    public Package2_Pengurus_Yayasan_Actor getPackage2_pengurus_yayasan_actor() {
        return package2_pengurus_yayasan_actor;
    }

    public void setPackage2_pengurus_yayasan_actor(Package2_Pengurus_Yayasan_Actor package2_pengurus_yayasan_actor) {
        this.package2_pengurus_yayasan_actor = package2_pengurus_yayasan_actor;
    }
    public Package2_Donatur_Actor getPackage2_donatur_actor() {
        return package2_donatur_actor;
    }

    public void setPackage2_donatur_actor(Package2_Donatur_Actor package2_donatur_actor) {
        this.package2_donatur_actor = package2_donatur_actor;
    }

}