





import java.util.List;
import java.util.ArrayList;

public class afpText_MMCRG  {

    private String value;
    private String key;





    private afpText_MMC afptext_mmc;


    public afpText_MMCRG(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public afpText_MMC getAfptext_mmc() {
        return afptext_mmc;
    }

    public void setAfptext_mmc(afpText_MMC afptext_mmc) {
        this.afptext_mmc = afptext_mmc;
    }

}