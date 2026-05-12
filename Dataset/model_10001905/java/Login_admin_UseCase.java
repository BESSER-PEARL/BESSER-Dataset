





import java.util.List;
import java.util.ArrayList;

public class Login_admin_UseCase  {






    private Input_data_service_UseCase input_data_service_usecase;




    private Input_data_kendaraan_UseCase input_data_kendaraan_usecase;




    private Input_data_kerusakan_UseCase input_data_kerusakan_usecase;




    private Input_data_pengemudi_UseCase input_data_pengemudi_usecase;




    private Input_data_mekanik_UseCase input_data_mekanik_usecase;


    public Login_admin_UseCase(
    ) {
    }



    public Input_data_service_UseCase getInput_data_service_usecase() {
        return input_data_service_usecase;
    }

    public void setInput_data_service_usecase(Input_data_service_UseCase input_data_service_usecase) {
        this.input_data_service_usecase = input_data_service_usecase;
    }
    public Input_data_kendaraan_UseCase getInput_data_kendaraan_usecase() {
        return input_data_kendaraan_usecase;
    }

    public void setInput_data_kendaraan_usecase(Input_data_kendaraan_UseCase input_data_kendaraan_usecase) {
        this.input_data_kendaraan_usecase = input_data_kendaraan_usecase;
    }
    public Input_data_kerusakan_UseCase getInput_data_kerusakan_usecase() {
        return input_data_kerusakan_usecase;
    }

    public void setInput_data_kerusakan_usecase(Input_data_kerusakan_UseCase input_data_kerusakan_usecase) {
        this.input_data_kerusakan_usecase = input_data_kerusakan_usecase;
    }
    public Input_data_pengemudi_UseCase getInput_data_pengemudi_usecase() {
        return input_data_pengemudi_usecase;
    }

    public void setInput_data_pengemudi_usecase(Input_data_pengemudi_UseCase input_data_pengemudi_usecase) {
        this.input_data_pengemudi_usecase = input_data_pengemudi_usecase;
    }
    public Input_data_mekanik_UseCase getInput_data_mekanik_usecase() {
        return input_data_mekanik_usecase;
    }

    public void setInput_data_mekanik_usecase(Input_data_mekanik_UseCase input_data_mekanik_usecase) {
        this.input_data_mekanik_usecase = input_data_mekanik_usecase;
    }

}