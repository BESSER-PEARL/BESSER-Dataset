





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_FilterExp  {

    private int number;





    private iOTConnector_ReadingNameWithConfigScope iotconnector_readingnamewithconfigscope;




    private iOTConnector_FilterExp iotconnector_filterexp;




    private iOTConnector_RelationalOperator iotconnector_relationaloperator;




    private iOTConnector_FilterAction iotconnector_filteraction;


    public iOTConnector_FilterExp(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public iOTConnector_ReadingNameWithConfigScope getIotconnector_readingnamewithconfigscope() {
        return iotconnector_readingnamewithconfigscope;
    }

    public void setIotconnector_readingnamewithconfigscope(iOTConnector_ReadingNameWithConfigScope iotconnector_readingnamewithconfigscope) {
        this.iotconnector_readingnamewithconfigscope = iotconnector_readingnamewithconfigscope;
    }
    public iOTConnector_FilterExp getIotconnector_filterexp() {
        return iotconnector_filterexp;
    }

    public void setIotconnector_filterexp(iOTConnector_FilterExp iotconnector_filterexp) {
        this.iotconnector_filterexp = iotconnector_filterexp;
    }
    public iOTConnector_RelationalOperator getIotconnector_relationaloperator() {
        return iotconnector_relationaloperator;
    }

    public void setIotconnector_relationaloperator(iOTConnector_RelationalOperator iotconnector_relationaloperator) {
        this.iotconnector_relationaloperator = iotconnector_relationaloperator;
    }
    public iOTConnector_FilterAction getIotconnector_filteraction() {
        return iotconnector_filteraction;
    }

    public void setIotconnector_filteraction(iOTConnector_FilterAction iotconnector_filteraction) {
        this.iotconnector_filteraction = iotconnector_filteraction;
    }

}