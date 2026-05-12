





import java.util.List;
import java.util.ArrayList;

public class Direktur_utama_Actor  {






    private Work_order_UseCase work_order_usecase;




    private Laporan_work_order_UseCase laporan_work_order_usecase;


    public Direktur_utama_Actor(
    ) {
    }



    public Work_order_UseCase getWork_order_usecase() {
        return work_order_usecase;
    }

    public void setWork_order_usecase(Work_order_UseCase work_order_usecase) {
        this.work_order_usecase = work_order_usecase;
    }
    public Laporan_work_order_UseCase getLaporan_work_order_usecase() {
        return laporan_work_order_usecase;
    }

    public void setLaporan_work_order_usecase(Laporan_work_order_UseCase laporan_work_order_usecase) {
        this.laporan_work_order_usecase = laporan_work_order_usecase;
    }

}