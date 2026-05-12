





import java.util.List;
import java.util.ArrayList;

public class Melakukan_pembayaran_UseCase  {






    private Melakukan_reservasi_kamar_UseCase melakukan_reservasi_kamar_usecase;


    public Melakukan_pembayaran_UseCase(
    ) {
    }



    public Melakukan_reservasi_kamar_UseCase getMelakukan_reservasi_kamar_usecase() {
        return melakukan_reservasi_kamar_usecase;
    }

    public void setMelakukan_reservasi_kamar_usecase(Melakukan_reservasi_kamar_UseCase melakukan_reservasi_kamar_usecase) {
        this.melakukan_reservasi_kamar_usecase = melakukan_reservasi_kamar_usecase;
    }

}