





import java.util.List;
import java.util.ArrayList;

public class Mahasiswa_Actor  {






    private Sistem_Mahasiswa_Login_UseCase sistem_mahasiswa_login_usecase;




    private Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase sistem_mahasiswa_update_data_mahasiswa_usecase;




    private Sistem_Mahasiswa_Melihat_Informasi_UseCase sistem_mahasiswa_melihat_informasi_usecase;




    private Sistem_Mahasiswa_Ganti_Password_UseCase sistem_mahasiswa_ganti_password_usecase;


    public Mahasiswa_Actor(
    ) {
    }



    public Sistem_Mahasiswa_Login_UseCase getSistem_mahasiswa_login_usecase() {
        return sistem_mahasiswa_login_usecase;
    }

    public void setSistem_mahasiswa_login_usecase(Sistem_Mahasiswa_Login_UseCase sistem_mahasiswa_login_usecase) {
        this.sistem_mahasiswa_login_usecase = sistem_mahasiswa_login_usecase;
    }
    public Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase getSistem_mahasiswa_update_data_mahasiswa_usecase() {
        return sistem_mahasiswa_update_data_mahasiswa_usecase;
    }

    public void setSistem_mahasiswa_update_data_mahasiswa_usecase(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase sistem_mahasiswa_update_data_mahasiswa_usecase) {
        this.sistem_mahasiswa_update_data_mahasiswa_usecase = sistem_mahasiswa_update_data_mahasiswa_usecase;
    }
    public Sistem_Mahasiswa_Melihat_Informasi_UseCase getSistem_mahasiswa_melihat_informasi_usecase() {
        return sistem_mahasiswa_melihat_informasi_usecase;
    }

    public void setSistem_mahasiswa_melihat_informasi_usecase(Sistem_Mahasiswa_Melihat_Informasi_UseCase sistem_mahasiswa_melihat_informasi_usecase) {
        this.sistem_mahasiswa_melihat_informasi_usecase = sistem_mahasiswa_melihat_informasi_usecase;
    }
    public Sistem_Mahasiswa_Ganti_Password_UseCase getSistem_mahasiswa_ganti_password_usecase() {
        return sistem_mahasiswa_ganti_password_usecase;
    }

    public void setSistem_mahasiswa_ganti_password_usecase(Sistem_Mahasiswa_Ganti_Password_UseCase sistem_mahasiswa_ganti_password_usecase) {
        this.sistem_mahasiswa_ganti_password_usecase = sistem_mahasiswa_ganti_password_usecase;
    }

}