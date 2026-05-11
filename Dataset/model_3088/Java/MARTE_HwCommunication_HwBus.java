





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwCommunication_HwBus extends HwMedia {

    private String wordWidth;
    private String isSynchronous;
    private String isSerial;
    private String adressWidth;



    public MARTE_HwCommunication_HwBus(
        String wordWidth,        String isSynchronous,        String isSerial,        String adressWidth    ) {
        super(
        );
        this.wordWidth = wordWidth;
        this.isSynchronous = isSynchronous;
        this.isSerial = isSerial;
        this.adressWidth = adressWidth;
    }


    public String getWordwidth() {
        return wordWidth;
    }

    public void setWordwidth(String wordWidth) {
        this.wordWidth = wordWidth;
    }
    public String getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(String isSynchronous) {
        this.isSynchronous = isSynchronous;
    }
    public String getIsserial() {
        return isSerial;
    }

    public void setIsserial(String isSerial) {
        this.isSerial = isSerial;
    }
    public String getAdresswidth() {
        return adressWidth;
    }

    public void setAdresswidth(String adressWidth) {
        this.adressWidth = adressWidth;
    }


}