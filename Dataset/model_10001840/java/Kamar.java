





import java.util.List;
import java.util.ArrayList;

public class Kamar  {

    private int no_kamar;
    private String tipe;
    private String _attr;
    private int jumlah_bed;
    private String status;



    public Kamar(
        int no_kamar,        String tipe,        String _attr,        int jumlah_bed,        String status    ) {
        this.no_kamar = no_kamar;
        this.tipe = tipe;
        this._attr = _attr;
        this.jumlah_bed = jumlah_bed;
        this.status = status;
    }


    public int getNo_kamar() {
        return no_kamar;
    }

    public void setNo_kamar(int no_kamar) {
        this.no_kamar = no_kamar;
    }
    public String getTipe() {
        return tipe;
    }

    public void setTipe(String tipe) {
        this.tipe = tipe;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public int getJumlah_bed() {
        return jumlah_bed;
    }

    public void setJumlah_bed(int jumlah_bed) {
        this.jumlah_bed = jumlah_bed;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}