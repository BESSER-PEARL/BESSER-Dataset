





import java.util.List;
import java.util.ArrayList;

public class Denda  {

    private int jumlah;
    private int ID_Denda;
    private String keterangan;
    private int ID_Reservasi;





    private ReservasiKamar reservasikamar;


    public Denda(
        int jumlah,        int ID_Denda,        String keterangan,        int ID_Reservasi    ) {
        this.jumlah = jumlah;
        this.ID_Denda = ID_Denda;
        this.keterangan = keterangan;
        this.ID_Reservasi = ID_Reservasi;
    }


    public int getJumlah() {
        return jumlah;
    }

    public void setJumlah(int jumlah) {
        this.jumlah = jumlah;
    }
    public int getId_denda() {
        return ID_Denda;
    }

    public void setId_denda(int ID_Denda) {
        this.ID_Denda = ID_Denda;
    }
    public String getKeterangan() {
        return keterangan;
    }

    public void setKeterangan(String keterangan) {
        this.keterangan = keterangan;
    }
    public int getId_reservasi() {
        return ID_Reservasi;
    }

    public void setId_reservasi(int ID_Reservasi) {
        this.ID_Reservasi = ID_Reservasi;
    }

    public ReservasiKamar getReservasikamar() {
        return reservasikamar;
    }

    public void setReservasikamar(ReservasiKamar reservasikamar) {
        this.reservasikamar = reservasikamar;
    }

}