





import java.util.List;
import java.util.ArrayList;

public class Banner  {

    private int IsShow;
    private String DateStart;
    private int BannerID;
    private String BannerInfo;
    private String DateEnd;
    private String Image;



    public Banner(
        int IsShow,        String DateStart,        int BannerID,        String BannerInfo,        String DateEnd,        String Image    ) {
        this.IsShow = IsShow;
        this.DateStart = DateStart;
        this.BannerID = BannerID;
        this.BannerInfo = BannerInfo;
        this.DateEnd = DateEnd;
        this.Image = Image;
    }


    public int getIsshow() {
        return IsShow;
    }

    public void setIsshow(int IsShow) {
        this.IsShow = IsShow;
    }
    public String getDatestart() {
        return DateStart;
    }

    public void setDatestart(String DateStart) {
        this.DateStart = DateStart;
    }
    public int getBannerid() {
        return BannerID;
    }

    public void setBannerid(int BannerID) {
        this.BannerID = BannerID;
    }
    public String getBannerinfo() {
        return BannerInfo;
    }

    public void setBannerinfo(String BannerInfo) {
        this.BannerInfo = BannerInfo;
    }
    public String getDateend() {
        return DateEnd;
    }

    public void setDateend(String DateEnd) {
        this.DateEnd = DateEnd;
    }
    public String getImage() {
        return Image;
    }

    public void setImage(String Image) {
        this.Image = Image;
    }


}