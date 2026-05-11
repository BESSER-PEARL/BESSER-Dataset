





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_FilterAction  {

    private int number;





    private iOTConnector_Filter iotconnector_filter;




    private iOTConnector_ReadingName iotconnector_readingname;


    public iOTConnector_FilterAction(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public iOTConnector_Filter getIotconnector_filter() {
        return iotconnector_filter;
    }

    public void setIotconnector_filter(iOTConnector_Filter iotconnector_filter) {
        this.iotconnector_filter = iotconnector_filter;
    }
    public iOTConnector_ReadingName getIotconnector_readingname() {
        return iotconnector_readingname;
    }

    public void setIotconnector_readingname(iOTConnector_ReadingName iotconnector_readingname) {
        this.iotconnector_readingname = iotconnector_readingname;
    }

}