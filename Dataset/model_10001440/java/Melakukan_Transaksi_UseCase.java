





import java.util.List;
import java.util.ArrayList;

public class Melakukan_Transaksi_UseCase  {






    private Admin_Actor admin_actor;




    private Pelanggan__Actor pelanggan__actor;


    public Melakukan_Transaksi_UseCase(
    ) {
    }



    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }
    public Pelanggan__Actor getPelanggan__actor() {
        return pelanggan__actor;
    }

    public void setPelanggan__actor(Pelanggan__Actor pelanggan__actor) {
        this.pelanggan__actor = pelanggan__actor;
    }

}