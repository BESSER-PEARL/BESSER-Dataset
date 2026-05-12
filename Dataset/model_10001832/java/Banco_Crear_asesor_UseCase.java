





import java.util.List;
import java.util.ArrayList;

public class Banco_Crear_asesor_UseCase  {






    private Banco_Iniciar_sesi_n_UseCase banco_iniciar_sesi_n_usecase;


    public Banco_Crear_asesor_UseCase(
    ) {
    }



    public Banco_Iniciar_sesi_n_UseCase getBanco_iniciar_sesi_n_usecase() {
        return banco_iniciar_sesi_n_usecase;
    }

    public void setBanco_iniciar_sesi_n_usecase(Banco_Iniciar_sesi_n_UseCase banco_iniciar_sesi_n_usecase) {
        this.banco_iniciar_sesi_n_usecase = banco_iniciar_sesi_n_usecase;
    }

}