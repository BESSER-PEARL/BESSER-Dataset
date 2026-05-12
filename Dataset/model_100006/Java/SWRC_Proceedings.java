





import java.util.List;
import java.util.ArrayList;

public class SWRC_Proceedings extends Publication {

    private String month;
    private String series;
    private String address;
    private String volume;
    private String number;



    public SWRC_Proceedings(
        String month,        String series,        String address,        String volume,        String number    ) {
        super(
        );
        this.month = month;
        this.series = series;
        this.address = address;
        this.volume = volume;
        this.number = number;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }


}