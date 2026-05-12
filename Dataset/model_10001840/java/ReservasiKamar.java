





import java.util.List;
import java.util.ArrayList;

public class ReservasiKamar  {

    private int no_kamar;
    private int NIK;
    private String tgl_start_booking;
    private String tgl_end_booking;
    private int ID_admin;
    private int ID_pembayaran;
    private int ID_Reservasi;





    private Admin admin;




    private Pemesan pemesan;




    private Kamar kamar;


    public ReservasiKamar(
        int no_kamar,        int NIK,        String tgl_start_booking,        String tgl_end_booking,        int ID_admin,        int ID_pembayaran,        int ID_Reservasi    ) {
        this.no_kamar = no_kamar;
        this.NIK = NIK;
        this.tgl_start_booking = tgl_start_booking;
        this.tgl_end_booking = tgl_end_booking;
        this.ID_admin = ID_admin;
        this.ID_pembayaran = ID_pembayaran;
        this.ID_Reservasi = ID_Reservasi;
    }


    public int getNo_kamar() {
        return no_kamar;
    }

    public void setNo_kamar(int no_kamar) {
        this.no_kamar = no_kamar;
    }
    public int getNik() {
        return NIK;
    }

    public void setNik(int NIK) {
        this.NIK = NIK;
    }
    public String getTgl_start_booking() {
        return tgl_start_booking;
    }

    public void setTgl_start_booking(String tgl_start_booking) {
        this.tgl_start_booking = tgl_start_booking;
    }
    public String getTgl_end_booking() {
        return tgl_end_booking;
    }

    public void setTgl_end_booking(String tgl_end_booking) {
        this.tgl_end_booking = tgl_end_booking;
    }
    public int getId_admin() {
        return ID_admin;
    }

    public void setId_admin(int ID_admin) {
        this.ID_admin = ID_admin;
    }
    public int getId_pembayaran() {
        return ID_pembayaran;
    }

    public void setId_pembayaran(int ID_pembayaran) {
        this.ID_pembayaran = ID_pembayaran;
    }
    public int getId_reservasi() {
        return ID_Reservasi;
    }

    public void setId_reservasi(int ID_Reservasi) {
        this.ID_Reservasi = ID_Reservasi;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Pemesan getPemesan() {
        return pemesan;
    }

    public void setPemesan(Pemesan pemesan) {
        this.pemesan = pemesan;
    }
    public Kamar getKamar() {
        return kamar;
    }

    public void setKamar(Kamar kamar) {
        this.kamar = kamar;
    }

}