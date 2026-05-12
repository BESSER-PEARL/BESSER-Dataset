




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Data_Pegawai  {

    private LocalDate tanggallahir;
    private String status;
    private int NIK;
    private String tempatlahir;
    private String Namakaryawan;
    private String alamat;



    public Data_Pegawai(
        LocalDate tanggallahir,        String status,        int NIK,        String tempatlahir,        String Namakaryawan,        String alamat    ) {
        this.tanggallahir = tanggallahir;
        this.status = status;
        this.NIK = NIK;
        this.tempatlahir = tempatlahir;
        this.Namakaryawan = Namakaryawan;
        this.alamat = alamat;
    }


    public LocalDate getTanggallahir() {
        return tanggallahir;
    }

    public void setTanggallahir(LocalDate tanggallahir) {
        this.tanggallahir = tanggallahir;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getNik() {
        return NIK;
    }

    public void setNik(int NIK) {
        this.NIK = NIK;
    }
    public String getTempatlahir() {
        return tempatlahir;
    }

    public void setTempatlahir(String tempatlahir) {
        this.tempatlahir = tempatlahir;
    }
    public String getNamakaryawan() {
        return Namakaryawan;
    }

    public void setNamakaryawan(String Namakaryawan) {
        this.Namakaryawan = Namakaryawan;
    }
    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }


}