





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_SampleAction  {

    private int amountOfTime;
    private int number;





    private iOTConnector_ReadingName iotconnector_readingname;




    private iOTConnector_Sample iotconnector_sample;


    public iOTConnector_SampleAction(
        int amountOfTime,        int number    ) {
        this.amountOfTime = amountOfTime;
        this.number = number;
    }


    public int getAmountoftime() {
        return amountOfTime;
    }

    public void setAmountoftime(int amountOfTime) {
        this.amountOfTime = amountOfTime;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public iOTConnector_ReadingName getIotconnector_readingname() {
        return iotconnector_readingname;
    }

    public void setIotconnector_readingname(iOTConnector_ReadingName iotconnector_readingname) {
        this.iotconnector_readingname = iotconnector_readingname;
    }
    public iOTConnector_Sample getIotconnector_sample() {
        return iotconnector_sample;
    }

    public void setIotconnector_sample(iOTConnector_Sample iotconnector_sample) {
        this.iotconnector_sample = iotconnector_sample;
    }

}