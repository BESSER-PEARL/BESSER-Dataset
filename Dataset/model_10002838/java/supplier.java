





import java.util.List;
import java.util.ArrayList;

public class supplier  {

    private String attribute;
    private String no_telp_supp;
    private int id_supplier;
    private None nama_supplier;
    private String alamat;



    public supplier(
        String attribute,        String no_telp_supp,        int id_supplier,        None nama_supplier,        String alamat    ) {
        this.attribute = attribute;
        this.no_telp_supp = no_telp_supp;
        this.id_supplier = id_supplier;
        this.nama_supplier = nama_supplier;
        this.alamat = alamat;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getNo_telp_supp() {
        return no_telp_supp;
    }

    public void setNo_telp_supp(String no_telp_supp) {
        this.no_telp_supp = no_telp_supp;
    }
    public int getId_supplier() {
        return id_supplier;
    }

    public void setId_supplier(int id_supplier) {
        this.id_supplier = id_supplier;
    }
    public None getNama_supplier() {
        return nama_supplier;
    }

    public void setNama_supplier(None nama_supplier) {
        this.nama_supplier = nama_supplier;
    }
    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }


}