





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwStorageManager_HwDMA extends HwCommunication_HwArbiter, HwStorageManager_HwStorageManager {

    private String nbChannels;
    private String transferWidth;



    public MARTE_HwStorageManager_HwDMA(
        String nbChannels,        String transferWidth    ) {
        super(
        );
        this.nbChannels = nbChannels;
        this.transferWidth = transferWidth;
    }


    public String getNbchannels() {
        return nbChannels;
    }

    public void setNbchannels(String nbChannels) {
        this.nbChannels = nbChannels;
    }
    public String getTransferwidth() {
        return transferWidth;
    }

    public void setTransferwidth(String transferWidth) {
        this.transferWidth = transferWidth;
    }


}