





import java.util.List;
import java.util.ArrayList;

public class testimoni  {

    private String info_instagram;
    private String sarana;
    private String ptn;
    private String akses_instagram;
    private String kepuasan_instagram;
    private String waktu_instagram;
    private String buka_instagram;
    private String mudah_info;
    private String kritik;
    private String pts_favorit;
    private int id;



    public testimoni(
        String info_instagram,        String sarana,        String ptn,        String akses_instagram,        String kepuasan_instagram,        String waktu_instagram,        String buka_instagram,        String mudah_info,        String kritik,        String pts_favorit,        int id    ) {
        this.info_instagram = info_instagram;
        this.sarana = sarana;
        this.ptn = ptn;
        this.akses_instagram = akses_instagram;
        this.kepuasan_instagram = kepuasan_instagram;
        this.waktu_instagram = waktu_instagram;
        this.buka_instagram = buka_instagram;
        this.mudah_info = mudah_info;
        this.kritik = kritik;
        this.pts_favorit = pts_favorit;
        this.id = id;
    }


    public String getInfo_instagram() {
        return info_instagram;
    }

    public void setInfo_instagram(String info_instagram) {
        this.info_instagram = info_instagram;
    }
    public String getSarana() {
        return sarana;
    }

    public void setSarana(String sarana) {
        this.sarana = sarana;
    }
    public String getPtn() {
        return ptn;
    }

    public void setPtn(String ptn) {
        this.ptn = ptn;
    }
    public String getAkses_instagram() {
        return akses_instagram;
    }

    public void setAkses_instagram(String akses_instagram) {
        this.akses_instagram = akses_instagram;
    }
    public String getKepuasan_instagram() {
        return kepuasan_instagram;
    }

    public void setKepuasan_instagram(String kepuasan_instagram) {
        this.kepuasan_instagram = kepuasan_instagram;
    }
    public String getWaktu_instagram() {
        return waktu_instagram;
    }

    public void setWaktu_instagram(String waktu_instagram) {
        this.waktu_instagram = waktu_instagram;
    }
    public String getBuka_instagram() {
        return buka_instagram;
    }

    public void setBuka_instagram(String buka_instagram) {
        this.buka_instagram = buka_instagram;
    }
    public String getMudah_info() {
        return mudah_info;
    }

    public void setMudah_info(String mudah_info) {
        this.mudah_info = mudah_info;
    }
    public String getKritik() {
        return kritik;
    }

    public void setKritik(String kritik) {
        this.kritik = kritik;
    }
    public String getPts_favorit() {
        return pts_favorit;
    }

    public void setPts_favorit(String pts_favorit) {
        this.pts_favorit = pts_favorit;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}