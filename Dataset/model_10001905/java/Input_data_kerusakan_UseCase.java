





import java.util.List;
import java.util.ArrayList;

public class Input_data_kerusakan_UseCase  {






    private Cetak_SPK_UseCase cetak_spk_usecase;




    private Admin_Actor admin_actor;


    public Input_data_kerusakan_UseCase(
    ) {
    }



    public Cetak_SPK_UseCase getCetak_spk_usecase() {
        return cetak_spk_usecase;
    }

    public void setCetak_spk_usecase(Cetak_SPK_UseCase cetak_spk_usecase) {
        this.cetak_spk_usecase = cetak_spk_usecase;
    }
    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }

}