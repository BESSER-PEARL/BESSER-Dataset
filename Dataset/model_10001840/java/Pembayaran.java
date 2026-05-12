





import java.util.List;
import java.util.ArrayList;

public class Pembayaran  {

    private int ID_Pembayaran;
    private String status;
    private int ID_Reservasi;
    private int jumlah;
    private String deadline_bayar;





    private ReservasiKamar reservasikamar;


    public Pembayaran(
        int ID_Pembayaran,        String status,        int ID_Reservasi,        int jumlah,        String deadline_bayar    ) {
        this.ID_Pembayaran = ID_Pembayaran;
        this.status = status;
        this.ID_Reservasi = ID_Reservasi;
        this.jumlah = jumlah;
        this.deadline_bayar = deadline_bayar;
    }


    public int getId_pembayaran() {
        return ID_Pembayaran;
    }

    public void setId_pembayaran(int ID_Pembayaran) {
        this.ID_Pembayaran = ID_Pembayaran;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getId_reservasi() {
        return ID_Reservasi;
    }

    public void setId_reservasi(int ID_Reservasi) {
        this.ID_Reservasi = ID_Reservasi;
    }
    public int getJumlah() {
        return jumlah;
    }

    public void setJumlah(int jumlah) {
        this.jumlah = jumlah;
    }
    public String getDeadline_bayar() {
        return deadline_bayar;
    }

    public void setDeadline_bayar(String deadline_bayar) {
        this.deadline_bayar = deadline_bayar;
    }

    public ReservasiKamar getReservasikamar() {
        return reservasikamar;
    }

    public void setReservasikamar(ReservasiKamar reservasikamar) {
        this.reservasikamar = reservasikamar;
    }

}