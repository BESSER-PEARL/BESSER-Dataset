





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_declarations_ComplexChannelPriority extends ChannelPriority {

    private String channelOperator;



    public timedAutomata_declarations_ComplexChannelPriority(
        String channelOperator    ) {
        super(
        );
        this.channelOperator = channelOperator;
    }


    public String getChanneloperator() {
        return channelOperator;
    }

    public void setChanneloperator(String channelOperator) {
        this.channelOperator = channelOperator;
    }


}