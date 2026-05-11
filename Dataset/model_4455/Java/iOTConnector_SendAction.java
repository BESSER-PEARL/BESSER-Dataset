





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_SendAction  {

    private int number;





    private iOTConnector_Send iotconnector_send;




    private iOTConnector_ReadingName iotconnector_readingname;




    private iOTConnector_RelationalOperator iotconnector_relationaloperator;


    public iOTConnector_SendAction(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public iOTConnector_Send getIotconnector_send() {
        return iotconnector_send;
    }

    public void setIotconnector_send(iOTConnector_Send iotconnector_send) {
        this.iotconnector_send = iotconnector_send;
    }
    public iOTConnector_ReadingName getIotconnector_readingname() {
        return iotconnector_readingname;
    }

    public void setIotconnector_readingname(iOTConnector_ReadingName iotconnector_readingname) {
        this.iotconnector_readingname = iotconnector_readingname;
    }
    public iOTConnector_RelationalOperator getIotconnector_relationaloperator() {
        return iotconnector_relationaloperator;
    }

    public void setIotconnector_relationaloperator(iOTConnector_RelationalOperator iotconnector_relationaloperator) {
        this.iotconnector_relationaloperator = iotconnector_relationaloperator;
    }

}