





import java.util.List;
import java.util.ArrayList;

public class Song  {

    private String sIMG_url;
    private String sName;
    private int sID;
    private String sDate;
    private String sArtist;
    private String sCateg;



    public Song(
        String sIMG_url,        String sName,        int sID,        String sDate,        String sArtist,        String sCateg    ) {
        this.sIMG_url = sIMG_url;
        this.sName = sName;
        this.sID = sID;
        this.sDate = sDate;
        this.sArtist = sArtist;
        this.sCateg = sCateg;
    }


    public String getSimg_url() {
        return sIMG_url;
    }

    public void setSimg_url(String sIMG_url) {
        this.sIMG_url = sIMG_url;
    }
    public String getSname() {
        return sName;
    }

    public void setSname(String sName) {
        this.sName = sName;
    }
    public int getSid() {
        return sID;
    }

    public void setSid(int sID) {
        this.sID = sID;
    }
    public String getSdate() {
        return sDate;
    }

    public void setSdate(String sDate) {
        this.sDate = sDate;
    }
    public String getSartist() {
        return sArtist;
    }

    public void setSartist(String sArtist) {
        this.sArtist = sArtist;
    }
    public String getScateg() {
        return sCateg;
    }

    public void setScateg(String sCateg) {
        this.sCateg = sCateg;
    }


}