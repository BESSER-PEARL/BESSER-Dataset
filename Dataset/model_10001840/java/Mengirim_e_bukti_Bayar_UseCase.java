





import java.util.List;
import java.util.ArrayList;

public class Mengirim_e_bukti_Bayar_UseCase  {






    private Admin_Actor admin_actor;




    private Melakukan_reservasi_kamar_UseCase melakukan_reservasi_kamar_usecase;


    public Mengirim_e_bukti_Bayar_UseCase(
    ) {
    }



    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }
    public Melakukan_reservasi_kamar_UseCase getMelakukan_reservasi_kamar_usecase() {
        return melakukan_reservasi_kamar_usecase;
    }

    public void setMelakukan_reservasi_kamar_usecase(Melakukan_reservasi_kamar_UseCase melakukan_reservasi_kamar_usecase) {
        this.melakukan_reservasi_kamar_usecase = melakukan_reservasi_kamar_usecase;
    }

}